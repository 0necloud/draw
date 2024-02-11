# GITHUB: 0necloud  
# draw.py version 1.0

import turtle
import time
import random
import tkinter as tk
from datetime import datetime
# from functools import cache
#import os

delay = 0
pen_color = "black" #default
canvas_color = "white" #default
option = "pen"
ink = False

scale_size = 0.5
distance = 10

scale = 1

filePath = ""

fileName = datetime.now() #Get current time
fileName = fileName.strftime("%m""%d""%M""%S""%f")
#command = f'convert {filePath}{fileName}.ps {fileName}.png'


def screen_gen():
    global wn
    #screen
    wn = turtle.Screen()
    wn.title("draw")
    wn.bgcolor(canvas_color)
    wn.setup(width=600, height=600)
    wn.tracer(0) #Turns off screen update

screen_gen()

def line_gen():
    global line
    #snek line
    line = turtle.Turtle()
    line.speed(0)
    line.shape("circle")
    line.pencolor("black")
    line.fillcolor("yellow")
    line.shapesize(scale_size)
    line.penup()
    line.direction = "stop"
    line.setheading(90)

line_gen()
line.goto(0,0)

def pen_size(chosen_size):
    global scale_size
    global distance
    global scale
    
    scale = chosen_size

    if scale == 1:
        scale_size = 0.5
        distance = 10

    elif scale == 2:
        scale_size = 1
        distance = 20

    elif scale == 3:
        scale_size = 1.5
        distance = 30

    elif scale == 4:
        scale_size = 2
        distance = 40


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)


#Functions
def settings():
    global displayer
    global top
    global chosen_size
    global size_scroll

    root = tk.Tk()
    top = tk.Toplevel()
    top.resizable(0,0)

    top.geometry('250x400') #Sets login GUI window size
    top.title('Settings') #Title of the window
    top.configure(background='light grey') #Background color

    label1 = tk.Label(top, text='SIZE\n',background='light grey') #Labels

    # button0= tk.Button(top, text='1', command=lambda:speed_1(), width=5) 
    # button1 = tk.Button(top, text='2', command=lambda:speed_2(),width=5) 
    # button2 = tk.Button(top, text='3', command=lambda:speed_3(),width=5) 
    # button3 = tk.Button(top, text='4', command=lambda:speed_4(),width=5) 

    size_scroll = tk.Scale(top, from_=1, to=4, orient=tk.HORIZONTAL, bg='light grey')

    label1.place(x=25,y=10) 
    # button0.pack(padx=(5,5), side=tk.LEFT) 
    # button1.pack(padx=(5,5), side=tk.LEFT) 
    # button2.pack(padx=(5,5), side=tk.LEFT) 
    # button3.pack(padx=(5,5), side=tk.LEFT) 

    # button0.place(x=25,y=35)
    # button1.place(x=75,y=35)
    # button2.place(x=125,y=35)
    # button3.place(x=175,y=35)

    size_scroll.place(x=25,y=33)
    chosen_size = size_scroll.get()

    #label2 = tk.Label(top, text='COLOR\n', background='light grey') #Labels
    pen_button = tk.Button(top, text="PEN", command=lambda:pen_c(), width=12)
    canvas_button = tk.Button(top, text="CANVAS", command=lambda:canvas_c(), width=12)
    buttona= tk.Button(top, command=lambda:color_1(), width=5, bg="blue") 
    buttonb = tk.Button(top, command=lambda:color_2(), width=5, bg="red") 
    buttonc = tk.Button(top, command=lambda:color_3(), width=5, bg="green")
    buttond = tk.Button(top, command=lambda:color_4(), width=5, bg="black")
    buttone = tk.Button(top, command=lambda:color_5(), width=5, bg="white")
    buttonf = tk.Button(top, command=lambda:color_6(), width=5, bg="purple")
    buttong = tk.Button(top, command=lambda:color_7(), width=5, bg="yellow")
    buttonh = tk.Button(top, command=lambda:color_8(), width=5, bg="orange")
    buttoni = tk.Button(top, command=lambda:color_9(), width=5, bg="grey")
    buttonj = tk.Button(top, command=lambda:color_10(), width=5, bg="pink")
    buttonk = tk.Button(top, command=lambda:color_11(), width=5, bg="brown")
    buttonl = tk.Button(top, command=lambda:color_12(), width=5, bg="cyan")

    pen_button.place(x=25,y=83)
    canvas_button.place(x=126,y=83)
    buttona.place(x=25,y=118)
    buttonb.place(x=75,y=118)
    buttonc.place(x=125,y=118) 
    buttond.place(x=175,y=118)
    buttone.place(x=25,y=158)
    buttonf.place(x=75,y=158)
    buttong.place(x=125,y=158)
    buttonh.place(x=175,y=158)
    buttoni.place(x=25,y=198)
    buttonj.place(x=75,y=198)
    buttonk.place(x=125,y=198)
    buttonl.place(x=175,y=198)
    
    # buttona.grid(column=0)
    # buttonb.grid(column=1)
    # buttonc.grid(column=2)
    # buttond.grid(column=3)

    displayer = tk.Text(top,width=24,height=5)
    displayer.place(x=25,y=238)

    launch_button = tk.Button(top, text='LAUNCH', command=lambda:close(), width=27)
    launch_button.place(x=25,y=343)
    displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
    displayer.configure(state='disabled')

    root.withdraw() #Hides root window  
    root.mainloop() #Runs event loop


#========================================================================================================================================================


def close():
    chosen_size = size_scroll.get()
    top.destroy()
    screen_gen()
    pen_size(chosen_size)
    draw()
    
def go_up():
    line.direction = "up"
    line.setheading(90)

def go_down():
    line.direction = "down"
    line.setheading(270)

def go_left():
    line.direction = "left"
    line.setheading(180)

def go_right():
    line.direction = "right"
    line.setheading(0)

def pause():
    line.direction = "stop"
    try:
        top.destroy()
    except:
        pass
    settings()

def clear():
    wn.bye()
    exit()
    # global counter

    # time.sleep(1)
    # line.goto(0,0)
    # line.direction = "stop"
    # counter = 0

def save():
    line.getscreen().getcanvas().postscript(file=f'{filePath}{fileName}.ps')
    #os.system(command)
    print(f"State saved to {filePath}")

def pen_down():
    global ink
    ink = True

def pen_up():
    global ink
    ink = False

def drawing():
    global ink

    if ink:
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(pen_color)
        new_segment.shapesize(scale_size)
        new_segment.penup()

        ink = False #reset

        x = line.xcor()
        y = line.ycor()
        new_segment.goto(x,y)

        
def reset():
    global line
    line.goto(1000,1000)
    line.clear()
    line_gen()
    line.goto(0,0)

#========================================================================================================================================================

#speed

# def speed_1():
#     global delay
#     delay = 1.5
#     try:
#         displayer.configure(state='normal')
#         displayer.delete('1.0',tk.END)
#         displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
#         displayer.configure(state='disabled')
#     except:
#         pass

# def speed_2():
#     global delay
#     delay = 1.0
#     try:
#         displayer.configure(state='normal')
#         displayer.delete('1.0',tk.END)
#         displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
#         displayer.configure(state='disabled')
#     except:
#         pass

# def speed_3():
#     global delay
#     delay = 0.5
#     try:
#         displayer.configure(state='normal')
#         displayer.delete('1.0',tk.END)
#         displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
#         displayer.configure(state='disabled')
#     except:
#         pass

# def speed_4():
#     global delay
#     delay = 0
#     try:
#         displayer.configure(state='normal')
#         displayer.delete('1.0',tk.END)
#         displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
#         displayer.configure(state='disabled')
#     except:
#         pass


#========================================================================================================================================================

#color

def color_1():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "blue"
    else:
        canvas_color = "blue"
        pen.color("white")

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_2():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "red"
    else:
        canvas_color = "red"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_3():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "green"
    else:
        canvas_color = "green"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_4():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "black"
    else:
        canvas_color = "black"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_5():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "white"
    else:
        canvas_color = "white"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_6():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "purple"
    else:
        canvas_color = "purple"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_7():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "yellow"
    else:
        canvas_color = "yellow"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_8():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "orange"
    else:
        canvas_color = "orange"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_9():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "grey"
    else:
        canvas_color = "grey"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_10():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "pink"
    else:
        canvas_color = "pink"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_11():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "brown"
    else:
        canvas_color = "brown"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass

def color_12():
    global pen_color
    global canvas_color

    if option == "pen":
        pen_color = "cyan"
    else:
        canvas_color = "cyan"

    try:
        displayer.configure(state='normal')
        displayer.delete('1.0',tk.END)
        displayer.insert(tk.END, f"SIZE: {scale} (CURRENT)\nCOLOR: {pen_color}\nCANVAS: {canvas_color}")
        displayer.configure(state='disabled')
    except:
        pass



def pen_c():
    global option
    option = "pen"

def canvas_c():
    global option
    option = "canvas"


#========================================================================================================================================================

# @cache
def draw():
    #Main Game Loop
    try:
        while True:
            wn.update()

            #pen.clear()
            #pen.write(f"{counter}",align="center",font=24)

            drawing()

            #Check for border collision
            if line.xcor() > 290 or line.xcor() < -290 or line.ycor() > 290 or line.ycor() < -290:
                time.sleep(1)
                line.goto(0,0)
                line.direction = "stop"

            move()

            time.sleep(delay)

    except:
        raise SystemExit(0)
    

    try:
        wn.mainloop()
    except:
        raise SystemExit(0)

def move():
    if line.direction == "up":
       y = line.ycor()
       line.sety(y+distance)


    if line.direction == "down":
       y = line.ycor()
       line.sety(y-distance)


    if line.direction == "left":
       x = line.xcor()
       line.setx(x-distance)


    if line.direction == "right":
       x = line.xcor()
       line.setx(x+distance)

    to_x = line.xcor()
    to_y = line.ycor()

    #line.goto(1000,1000)
    line.clear()
    line.ht()
    
    line_gen()
    line.goto(to_x,to_y)

#========================================================================================================================================================

#Key Bindings
wn.listen()

#movement
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

wn.onkeypress(pause,"p")
wn.onkeypress(clear,"c")

#pen
#wn.onkeypress(pen_down, "space")
wn.onkeyrelease(pen_down, "space")
#wn.onkeyrelease(pen_up, "space")

#speed
# wn.onkeypress(speed_1, "1")
# wn.onkeypress(speed_2, "2")
# wn.onkeypress(speed_3, "3")
# wn.onkeypress(speed_4, "4")

#color
# wn.onkeypress(color_1, "KP_1")
# wn.onkeypress(color_2, "KP_2")
# wn.onkeypress(color_3, "KP_3")
wn.onkeypress(color_4, "Return")
wn.onkeypress(color_5, "BackSpace")
# wn.onkeypress(color_6, "KP_6")
# wn.onkeypress(color_7, "KP_7")
# wn.onkeypress(color_8, "KP_8")

wn.onkeypress(reset,"r")
#wn.onkeypress(save,"o")

#========================================================================================================================================================


#Settings Menu
settings()
