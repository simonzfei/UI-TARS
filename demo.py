import base64
from openai import OpenAI


instruction = "click the Maps area"
screenshot_path = "/media/f/E/project/agentic/UI-TARS/figures/screenshot2.png"
client = OpenAI(
    base_url="http://0.0.0.0:8000/v1",
    api_key="empty",
)


## Below is the prompt for mobile
prompt = r"""You are a GUI agent. You are given a task and your action history, with screenshots. You need to perform the next action to complete the task. 

## Output Format
```\nThought: ...
Action: ...\n```

## Action Space

click(start_box='<|box_start|>(x1,y1)<|box_end|>')
left_double(start_box='<|box_start|>(x1,y1)<|box_end|>')
right_single(start_box='<|box_start|>(x1,y1)<|box_end|>')
drag(start_box='<|box_start|>(x1,y1)<|box_end|>', end_box='<|box_start|>(x3,y3)<|box_end|>')
hotkey(key='')
type(content='') #If you want to submit your input, use \"\
\" at the end of `content`.
scroll(start_box='<|box_start|>(x1,y1)<|box_end|>', direction='down or up or right or left')
wait() #Sleep for 5s and take a screenshot to check for any changes.
finished()
call_user() # Submit the task and call the user when the task is unsolvable, or when you need the user's help.


## Note
- Use Chinese in `Thought` part.
- Summarize your next action (with its target element) in one sentence in `Thought` part.

## User Instruction
"""

with open(screenshot_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
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
print(response.choices[0].message.content)