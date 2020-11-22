# 画面表示に関するクラス

import tkinter

class View:

    # インスタンス生成時にWindowタイトルを決定。
    def __init__(self, title):
        
        self.title = title

    def WindowView(self):    
        
        root = tkinter.Tk()

        root.title(self.title)

        root.geometry("800x600")

        label = tkinter.Label(root, text = "Hello,World")

        label.grid()

        root.mainloop()
