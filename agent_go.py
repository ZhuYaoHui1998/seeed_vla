from utils_agent import *           # 智能体Agent编排
import time
from utils_stt import *


def back_zero():
    print("back_zero()111")
    time.sleep(1)

def llm_led(text):
    print(text)

def vlm_move(text):
    print(text)


def agent_play(order):
    agent_plan_output = eval(agent_plan(order))
    # 遍历 function 列表
    for each in agent_plan_output["function"]:
        print('开始执行动作:', each)
        eval(each)
    #print('智能体编排动作如下:\n', agent_plan_output)


print("Welcome to the Recording and Speech-to-Text System!")
print("Press '1' to start recording, '2' to stop recording.")

while True:
    if keyboard.is_pressed('1'):
        print("Preparing to start recording...")
        start_recording()
        save_recording()
        print("Processing the recording file, please wait...")
        text=stt_func()
    # Send the transcription result as an alert
        agent_play(text)
    time.sleep(0.1)  # Reduce CPU usage

