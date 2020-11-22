# 画面表示に関するクラス

import tkinter as tk

class View:

    # インスタンス生成時にWindowタイトルを決定。
    def __init__(self, title):
        
        self.title = title

    def WindowView(self):    
        
        root = tk.Tk()

        root.title(self.title)

        root.geometry("800x600")

        img = tk.PhotoImage(file = "sample.png")

        canvas = tk.Canvas(root, width = 640, height = 480)

        canvas.create_rectangle(0, 0, 640, 480, fill='green')

        canvas.place(x = 80, y = 60)

        canvas.create_image(0, 0, anchor='nw', image = img)

        root.mainloop()
