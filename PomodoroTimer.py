from tkinter import *

window=Tk()
window.title("Pomodoro by @dhruva3223")
window.config(padx=100,pady=50,bg="black")
title_label=Label(text="Timer",fg="white",font=("arial",50),bg="black")
title_label.grid(column=1,row=0)

canvas=Canvas(width=230,height=224,bg="black",highlightthickness=0)
tomato_img=PhotoImage(file="Tomato.png")
canvas.create_image(115,112,image=tomato_img)
timer_text=canvas.create_text(115,135,text="00:00",fill="white",font=("arial",35,"bold"))
canvas.grid(column=1,row=1)

window.mainloop()