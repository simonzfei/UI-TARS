#!/usr/bin/env python3
import os
import io
import re
import time
import json
import wave
import argparse
import requests
import pyaudio
import pyautogui
import mss
from PIL import Image
from openai import OpenAI

##############################
# ASR Transcription Function #
##############################

def get_user_instruction_from_audio():
    """
    Records audio from the microphone for a fixed duration,
    saves it as a temporary WAV file, sends the file to the ASR server,
    and returns the transcription result.
    """
    # --- Audio recording parameters ---
    DURATION = 5.0  # seconds to record
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    print("Recording from microphone for {} seconds...".format(DURATION))
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    for _ in range(0, int(RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

    # --- Save recording to a temporary WAV file ---
    temp_audio_file = "temp_audio.wav"
    wf = wave.open(temp_audio_file, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

    # --- Send the audio file to the ASR server ---
    # You can adjust these values as needed.
    asr_host = "127.0.0.1"
    asr_port = 8001
    url = f"http://{asr_host}:{asr_port}/recognition"
    files = [
        (
            "audio",
            (
                os.path.basename(temp_audio_file),
                open(temp_audio_file, "rb"),
                "application/octet-stream",
            ),
        )
    ]
    print("Sending audio file to ASR server at", url)
    response = requests.post(url, files=files)
    transcription = response.text.strip()
    print("Transcription result:", transcription)
    
    # Optionally remove the temporary file.
    os.remove(temp_audio_file)
    return transcription

##############################
# GUI Agent Helper Functions #
##############################

# Configure your OpenAI endpoint.
client = OpenAI(
    base_url="http://0.0.0.0:8000/v1",
    api_key="empty",
)

# Prompt for the GUI agent.
prompt = r"""You are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. 

## Output Format

Thought: ...
Action: ...

## Action Space

click(start_box='<|box_start|>(x1,y1)<|box_end|>')
left_double(start_box='<|box_start|>(x1,y1)<|box_end|>')
right_single(start_box='<|box_start|>(x1,y1)<|box_end|>')
drag(start_box='<|box_start|>(x1,y1)<|box_end|>', end_box='<|box_start|>(x3,y3)<|box_end|>')
hotkey(key='')
type(content='') #If you want to submit your input, use "\" at the end of `content`.
scroll(start_box='<|box_start|>(x1,y1)<|box_end|>', direction='down or up or right or left')
wait() #Sleep for 5s and take a screenshot to check for any changes.
finished()
call_user() # Submit the task and call the user when the task is unsolvable, or when you need the user's help.

## Note
- Use Chinese in the `Thought` part.
- Summarize your next action (with its target element) in one sentence in the `Thought` part.

## User Instruction:
"""

def capture_screen(save_path=None):
    """
    Capture the current screen, optionally save it to the provided path,
    and return a base64-encoded PNG image string.
    """
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        if save_path:
            img.save(save_path, format="PNG")
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        encoded_img = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_img

def parse_action_from_response(response_text):
    """
    Parse the model's response to extract an action command and its coordinates.
    Expected format example:
      Action: click(start_box='(218,356)')
    """
    pattern = r"Action:\s*(\w+)\(start_box='[(](\d+),\s*(\d+)[)]'\)"
    match = re.search(pattern, response_text)
    print("match:", match)
    if match:
        action_type = match.group(1)
        x = int(match.group(2))
        y = int(match.group(3))
        return action_type, x, y
    else:
        return None

def execute_action(action_type, x, y):
    """
    Execute a GUI action using PyAutoGUI based on the parsed action type and coordinates.
    Supports click, left_double, and right_single.
    """
    pyautogui.moveTo(x, y, duration=0.2)
    if action_type == "click":
        pyautogui.click()
    elif action_type == "left_double":
        pyautogui.doubleClick()
    elif action_type == "right_single":
        pyautogui.rightClick()
    time.sleep(1)

#########################
# Main Agent Loop Logic #
#########################

def main_loop():
    """
    Continuously capture the screen and send it to the model along with the current instruction and conversation history.
    Uses the audio-transcribed instruction obtained via ASR.
    
    If the model returns "call_user()", a new instruction is obtained via ASR.
    Each screenshot is saved in the "screenshots" folder.
    """
    os.makedirs("screenshots", exist_ok=True)

    # Get the initial instruction via ASR.
    user_instruction = get_user_instruction_from_audio()
    conversation_history = ""
    iteration = 0

    while True:
        print(f"Iteration {iteration}: Capturing screen...")
        save_path = os.path.join("screenshots", f"screenshot_{iteration}.png")
        encoded_string = capture_screen(save_path)

        full_prompt = prompt + user_instruction + "\n" + conversation_history
        print("Sending image and instructions to model...")

        response = client.chat.completions.create(
            model="ui-tars",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": full_prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded_string}"}},
                    ],
                },
            ],
            frequency_penalty=1,
            max_tokens=128,
        )
        response_text = response.choices[0].message.content
        print("Response from model:")
        print(response_text)

        if "finished()" in response_text:
            print("Received finished() command. Exiting loop.")
            break

        # If the model requests user input.
        if "call_user()" in response_text:
            print("Received call_user() command. 请通过语音输入新的指令...")
            user_instruction = get_user_instruction_from_audio()
            conversation_history += "\n" + response_text
            iteration += 1
            time.sleep(2)
            continue

        parsed = parse_action_from_response(response_text)
        if not parsed:
            print("No valid action found in response. Skipping execution this iteration.")
        else:
            action_type, x, y = parsed
            print(f"Executing action: {action_type} at ({x}, {y})")
            execute_action(action_type, x, y)

        conversation_history += "\n" + response_text
        print("conversation_history:", conversation_history)
        iteration += 1
        time.sleep(4)

    print("Agent loop finished.")

if __name__ == "__main__":
    # main_loop()
    get_user_instruction_from_audio()
