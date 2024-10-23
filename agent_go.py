
# 导入常用函数
# from utils_asr import *             # 录音+语音识别
# from utils_robot import *           # 连接机械臂
# from utils_llm import *             # 大语言模型API
# from utils_led import *             # 控制LED灯颜色
# from utils_camera import *          # 摄像头
# from utils_robot import *           # 机械臂运动
# from utils_pump import *            # GPIO、吸泵
# from utils_vlm_move import *        # 多模态大模型识别图像，吸泵吸取并移动物体
# from utils_drag_teaching import *   # 拖动示教
from utils_agent import *           # 智能体Agent编排
import time


def back_zero():
    print("back_zero()111")
    time.sleep(1)

def llm_led(text):
    print(text)

def vlm_move(text):
    print(text)


def agent_play():
    start_record_ok = input('是否开启录音，输入数字录音指定时长，按k打字输入，按c输入默认指令\n')
    if start_record_ok == 'k':
        order = input('请输入指令')
    elif start_record_ok == 'c':
        order = '先归零，再摇头，然后把绿色方块放在篮球上'
    else:
        print('无指令，退出')
        # exit()
        raise NameError('无指令，退出')
    agent_plan_output = eval(agent_plan(order))
    # 遍历 function 列表
    for each in agent_plan_output["function"]:
        print('开始执行动作:', each)
        eval(each)
    print('智能体编排动作如下:\n', agent_plan_output)

if __name__ == '__main__':
    agent_play()

