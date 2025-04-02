#!/usr/bin/env python3
import base64
import io
import time
import re
import pyautogui
import mss
from PIL import Image
from openai import OpenAI

# Configure your API endpoint and API key
client = OpenAI(
    base_url="http://0.0.0.0:8000/v1",
    api_key="empty",
)

instruction = "打开火狐浏览器"

prompt = r"""You are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. 

## Output Format

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
- Use Chinese in `Thought` part.
- Summarize your next action (with its target element) in one sentence in `Thought` part.

## User Instruction
"""

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
    # Add other actions as needed.
    time.sleep(1)

def parse_action_from_response(response_text):
    """
    Parses the model's response to extract the action and coordinates.
    Expected format example:
    
    Action: click(start_box='(218,356)')
    """
    # Updated regex to match the current output format without the <|box_start|> wrappers.
    pattern = r"Action:\s*(\w+)\(start_box='[(](\d+),\s*(\d+)[)]'\)"
    match = re.search(pattern, response_text)
    if match:
        action_type = match.group(1)
        x = int(match.group(2))
        y = int(match.group(3))
        return action_type, x, y
    else:
        return None 

def capture_screen():
    """
    Capture the current screen and return a base64-encoded PNG image string.
    """
    with mss.mss() as sct:
        # Capture the first monitor; adjust index if needed.
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        encoded_img = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_img

def main():
    # Capture the current screen.
    encoded_string = capture_screen()

    response = client.chat.completions.create(
        model="ui-tars",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt + instruction},
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

    parsed = parse_action_from_response(response_text)
    if not parsed:
        print("No valid action found in response. Exiting.")
    else:
        action_type, x, y = parsed
        print(f"Executing action: {action_type} at ({x}, {y})")
        execute_action(action_type, x, y)

if __name__ == "__main__":
    main()
