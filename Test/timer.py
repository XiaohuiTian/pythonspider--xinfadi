# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=root.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


# str = "bb649c83dd1ea5c9d9dec9a18df0ffe9"
# print(len(str))

# python 打印当前日期

# import time
# ti = time.strftime("%Y-%m-%d",time.localtime(time.time()))
# ad = ti >= '2016-12-21'
# print(ad)
# print(ti)
# c5643db2356fa9879e9e6a1d594a790e dingyu


# python 定时任务
#
# import schedule
# import time
#
# def job():
#     print("hello world")
#
# schedule.every(5).seconds.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
