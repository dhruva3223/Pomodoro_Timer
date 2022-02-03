from tkinter import *
WORK_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20
rep=0
timer=None

def reset_clock():
    pass

#timer aLgorithm
def start_clock():
    global rep
    rep+=1
    long_break_second=LONG_BREAK_TIME*60
    short_break_second=SHORT_BREAK_TIME*60
    work_second=WORK_TIME*60
    
    if rep%8==0:
        count_down(long_break_second)
        title_label.config(text="Break",fg="red")
    elif rep%2==0:
        count_down(short_break_second)
        title_label.config(text="Break",fg="pink")
    else:
        count_down(work_second)
        title_label.config(text="Work",fg="green")

#countdown algorithm
def count_down(clock_time):
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

#start button
start_button=Button(text="Start",highlightthickness=0,command=start_clock)
start_button.grid(column=0,row=2)

#reset button
reset_button=Button(text="Reset",highlightthickness=0,command=reset_clock)
reset_button.grid(column=2,row=2)

window.mainloop()