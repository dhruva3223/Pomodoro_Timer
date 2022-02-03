from tkinter import *

window=Tk()
window.title("Pomodoro by @dhruva3223")
window.config(padx=100,pady=50,bg="black")
title_label=Label(text="Timer",fg="white",font=("arial",50),bg="black")
title_label.grid(column=1,row=0)
window.mainloop()