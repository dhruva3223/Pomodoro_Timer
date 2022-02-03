from tkinter import *

def reset_timer():
    pass

def start_timer():
    pass

#tkinter window setting
window=Tk()
window.title("Pomodoro by @dhruva3223")
window.config(padx=100,pady=50,bg="black")
title_label=Label(text="Timer",fg="white",font=("arial",50),bg="black")
title_label.grid(column=1,row=0)

#canvas
canvas=Canvas(width=230,height=224,bg="black",highlightthickness=0)
tomato_img=PhotoImage(file="Tomato.png")
canvas.create_image(115,112,image=tomato_img)
timer_text=canvas.create_text(115,135,text="00:00",fill="white",font=("arial",35,"bold"))
canvas.grid(column=1,row=1)

#start/reset Button
start_timer=Button(text="Start",highlightthickness=0,command=start_timer)
start_timer.grid(column=0,row=2)

reset_timer=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_timer.grid(column=2,row=2)

window.mainloop()