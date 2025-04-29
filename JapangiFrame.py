from tkinter import *

class JapangiFrame(Frame):
    def __init__ (self, master):
        img = PhotoImage(file="/resource/images.png")
        lbl = Label(image = img)
        lbl.image = img #레퍼런스 추가?
        lbl.place(x = 150, y = 100)
        

        #참고: https://m.blog.naver.com/gaussian37/221057243324