#!/usr/bin/env python3
import base64
import io
import time
import re
import os
import pyautogui
import mss
from PIL import Image
from openai import OpenAI

# Configure your API endpoint and API key
client = OpenAI(
    base_url="http://0.0.0.0:8000/v1",
    api_key="empty",
)

# Prompt for computer GUI agent
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
    Capture the current screen, save the image if a save_path is provided,
    and return a base64-encoded PNG image string.
    """
    with mss.mss() as sct:
        # Capture the first monitor; adjust index if needed.
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        
        # Save the image if a save_path is provided.
        if save_path:
            img.save(save_path, format="PNG")
        
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        encoded_img = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_img


def parse_action_from_response(response_text):
    """
    Parses the model's response to extract the action and coordinates.
    Expected format example:
    
    Action: click(start_box='(218,356)')
    """
    pattern = r"Action:\s*(\w+)\(start_box='[(](\d+),\s*(\d+)[)]'\)"
    match = re.search(pattern, response_text)
    print('match:', match)
    if match:
        action_type = match.group(1)
        x = int(match.group(2))
        y = int(match.group(3))
        return action_type, x, y
    else:
        return None

def execute_action(action_type, x, y):
    """
    Executes the parsed action using PyAutoGUI.
    Currently supports:
      - click: single click
      - left_double: double left-click
      - right_single: right-click

    Extend this function to support drag, hotkey, type, scroll, etc.
    """
    pyautogui.moveTo(x, y, duration=0.2)
    if action_type == "click":
        pyautogui.click()
    elif action_type == "left_double":
        pyautogui.doubleClick()
    elif action_type == "right_single":
        pyautogui.rightClick()
    time.sleep(1)

def main_loop():
    """
    Continuously capture the screen, send it to the model with the instruction and conversation history,
    parse the returned action, and execute it.
    
    When the model returns "call_user()", the user is prompted for a new instruction,
    a new screenshot is captured, and the loop continues.
    """
    # Get the initial user instruction.
    user_instruction = input("请输入初始指令: ")
    conversation_history = ""
    iteration = 0

    # Ensure the screenshots folder exists.
    os.makedirs("screenshots", exist_ok=True)


    while True:
        print(f"Iteration {iteration}: Capturing screen...")
        save_path = os.path.join("screenshots", f"screenshot_{iteration}.png")
        encoded_string = capture_screen(save_path)

        # Create the full prompt including conversation history.
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

        # Check for termination instructions.
        if "finished()" in response_text:
            print("Received finished() command. Exiting loop.")
            break

        # If the model requests user input, prompt for new instruction.
        if "call_user()" in response_text:
            print("Received call_user() command. 请重新输入指令：")
            user_instruction = input("新指令: ")
            # Append response to conversation history and continue to next iteration.
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

        # Append the response to the conversation history for context.
        conversation_history += "\n" + response_text
        print("conversation_history:", conversation_history)

        iteration += 1
        # Optionally sleep before the next iteration.
        time.sleep(4)

    print("Agent loop finished.")

if __name__ == "__main__":
    main_loop()
