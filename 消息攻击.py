import time
from pynput import mouse,keyboard


time.sleep(2)  # 预留2秒用于准备
m_mouse = mouse.Controller()
m_keyboard = keyboard.Controller()  # 创建鼠标及键盘

# 请确保鼠标在聊天框内
m_mouse.click(mouse.Button.left)  # 点击鼠标左键

for a in range(20):  # 这里输入发信息的次数
    m_keyboard.type('冯正扬好傻冯正扬好傻！！！！！')  # 这里输入你要发的字
    m_keyboard.press(keyboard.Key.enter)  # 按下enter发送
    m_keyboard.release(keyboard.Key.enter)  # 释放enter
    time.sleep(0.5)  # 这里调整频率(一次发送后的等待时间)