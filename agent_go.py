from utils_agent import *           # 智能体Agent编排
import time
from utils_stt import *
import pyaudio
import wave

def back_zero():
    print("back_zero()111")
    time.sleep(1)

def llm_led(text):
    print(text)

def vlm_move(text):
    print(text)

def mic_init():
    audio = pyaudio.PyAudio()
    print("Available audio input devices:")
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']} - {info['maxInputChannels']} channels")
    device_index = int(input("Please select the device index for your USB microphone: "))
    device_info = audio.get_device_info_by_index(device_index)
    supported_sample_rates = [8000, 16000, 32000, 44100, 48000]
    supported_rate=0
    for rate in supported_sample_rates:
        try:
            if audio.is_format_supported(rate,
                                        input_device=device_index,
                                        input_channels=1,
                                        input_format=pyaudio.paInt16):
                supported_rate=rate
                print(f"{rate} Hz is supported.")
        except ValueError:
            print(f"{rate} Hz is not supported.")
    return device_index,supported_rate

def agent_play(order):
    agent_plan_output = eval(agent_plan(order))
    # 遍历 function 列表
    for each in agent_plan_output["function"]:
        print('开始执行动作:', each)
        eval(each)
    #print('智能体编排动作如下:\n', agent_plan_output)


print("Welcome to the Recording and Speech-to-Text System!")
device_index,supported_rate=mic_init()
print("Press '1' to start recording, '2' to stop recording.")



while True:
    if keyboard.is_pressed('1'):
        print("Preparing to start recording...")
        start_recording(device_index,supported_rate)
        save_recording()
        print("Processing the recording file, please wait...")
        text=stt_func()
    # Send the transcription result as an alert
        agent_play(text)
    time.sleep(0.1)  # Reduce CPU usage

