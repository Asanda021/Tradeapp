import tkinter as tk
from tkinter import ttk
class TradeappWindows:
    def __init__(self,root=None):
        self.root=root or tk.Tk(); self.root.title("Tradeapp"); self.root.geometry("900x600")
        self.status=tk.StringVar(value="آماده")
        ttk.Label(self.root,text="Tradeapp",font=("Segoe UI",20)).pack(pady=20)
        ttk.Label(self.root,textvariable=self.status).pack(pady=10)
        ttk.Button(self.root,text="شروع حالت آزمایشی",command=lambda:self.status.set("حالت آزمایشی فعال شد")).pack()
    def run(self): self.root.mainloop()
if __name__=="__main__": TradeappWindows().run()
