from tkinter import *
import math
WORK_TIME = 0.05
SHORT_BREAK_TIME = 0.05
LONG_BREAK_TIME = 20
rep=0
timer=None

#Making start button visible
def start_button_visible():
    start_button=Button(text="Start",highlightthickness=0,command=start_clock)
    start_button.grid(column=0,row=2)

#Rest clock
def reset_clock():
    window.after_cancel(timer)
    title_label.config(text="Timer",fg="green")
    canvas.itemconfig(timer_text,text="00:00")
    start_button_visible()

#timer aLgorithm
def start_clock():
    start_button.grid_forget()
    dummy_button=Button(text="Start",highlightthickness=0)
    dummy_button.grid(column=0,row=2)
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
    count_minute=math.floor(clock_time/60)
    count_second=clock_time%60
    if count_second<10:
        count_second=f"0{count_second}"
    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_second}")
    if clock_time>0:
        global timer
        timer=window.after(1000,count_down,clock_time-1)
    if clock_time==0:
        window.attributes("-topmost", True)
        window.attributes('-topmost', 0)
        start_button_visible()
    else:
        tick=""
        round_completed=math.floor(rep/2)
        for _ in range(round_completed):
            tick+="✔"
        tick_mark.config(text=tick)


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

tick_mark=Label(text="",fg="green",bg="black")
tick_mark.grid(column=1,row=3)

window.mainloop()