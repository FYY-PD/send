import time
from pynput import mouse, keyboard
import tkinter as tk


class GUIApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("聊天信息发送器")
        self.root.geometry("300x250")  # 增加窗口高度以容纳倒计时和提示标签
        self.root.resizable(False, False)  # 禁止用户改变窗口大小

        self.message_entry = tk.Entry(self.root, width=25)
        self.message_entry.pack(pady=(10, 0))

        self.send_button = tk.Button(self.root, text="开始发送", command=self.start_countdown)  # 修改command绑定和文本
        self.send_button.pack(pady=(10, 0))

        self.quit_button = tk.Button(self.root, text="退出应用", command=self.root.quit)
        self.quit_button.pack(pady=(10, 0))

        self.countdown_label = tk.Label(self.root, text="")
        self.countdown_label.pack(pady=(10, 10))

        self.instructions_label = tk.Label(self.root, text="注：当点击开始时开始计时，倒计时结束后将发送信息。\n按下开始后，请尽快将鼠标移到聊天框上。\n倒计时结束前点击退出可终止发送。")
        self.instructions_label.pack(side=tk.BOTTOM)

        self.m_mouse = mouse.Controller()
        self.m_keyboard = keyboard.Controller()

        self.countdown_time = 5  # 倒计时时间（秒）
        self.timer_running = False
        self.message_to_send = None  # 存储要发送的消息

    def start_countdown(self):
        self.message_to_send = self.message_entry.get()  # 获取输入框中的内容并存储
        if not self.timer_running:
            self.timer_running = True
            self.countdown_label.config(text=f"倒计时：{self.countdown_time} 秒")
            self.countdown()

    def countdown(self):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.countdown_label.config(text=f"倒计时：{self.countdown_time} 秒")
            self.root.after(1000, self.countdown)  # 每隔一秒执行一次countdown函数
        else:
            self.countdown_label.config(text="倒计时结束，开始发送消息...")
            self.timer_running = False
            self.send_message()  # 倒计时结束后调用发送消息函数

    def send_message(self):
        # 确保鼠标在聊天框内（这部分需根据实际情况编写）
        time.sleep(2)
        self.m_mouse.click(mouse.Button.left)

        for _ in range(10):  # 这里输入发信息的次数
            self.m_keyboard.type(self.message_to_send)  # 使用self.m_keyboard引用键盘控制器
            self.m_keyboard.press(keyboard.Key.enter)  # 按下enter发送
            self.m_keyboard.release(keyboard.Key.enter)  # 释放enter
            time.sleep(0.5)  # 这里调整频率(一次发送后的等待时间)

        self.message_entry.delete(0, 'end')  # 清空输入框（若需要）
        self.root.update_idletasks()  # 更新窗口状态

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GUIApplication()
    app.run()
