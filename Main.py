import Functions as fs
import tkinter as tk
import pandas as pd
from functools import partial
from math import sqrt

color = "red"

window = tk.Tk()
window.title("Calculator")
window.geometry("230x275")
window.configure(bg=color)

frame_top = tk.Frame(master=window, width=50, height=100, bg=color)
frame_bot = tk.Frame(master=window, width=50, height=100, bg=color)
frame_bot2 = tk.Frame(master=window, width=50, height=100)

frame_bot.rowconfigure(4, minsize=20)
frame_bot.columnconfigure([0, 1, 2], minsize=20)

frame_top.pack()
frame_bot.pack(side=tk.LEFT, padx=3, pady=5)
frame_bot2.pack(side=tk.RIGHT, padx=3, pady=5)

banner = tk.Label(
    master=frame_top,
    text="Calculator v1.0",
    foreground="yellow",
    background="black",
    width=35)
banner.pack()

display = tk.Label(
    master=frame_top,
    text=0,
    width=20,
    bg="white",
    justify=tk.RIGHT,
    anchor=tk.E,
    relief=tk.SUNKEN)
display.pack()

number = list()
for i in range(3):
    for j in range(3):
        number.append(tk.Button(
            master=frame_bot,
            text=str(j+1 + i*3),
            foreground="black",
            background="light grey",
            width=6,
            height=3,
            command=partial(fs.GetInput, display, j+1 + i*3)
            ))
        number[-1].grid(row = i, column = j)

number.append(tk.Button(
    master=frame_bot,
    text="0",
    foreground="black",
    background="light grey",
    width=6,
    height=3,
    command=partial(fs.GetInput, display, 0)
    ))
number[-1].grid(row = 3, column = 0, columnspan=2, sticky = tk.W+tk.E)

number.append(tk.Button(
    master=frame_bot,
    text=".",
    foreground="black",
    background="light grey",
    width=6,
    height=3,
    command=partial(fs.GetInput, display, ".")
    ))
number[-1].grid(row = 3, column = 2)

global numbers_q, operations_q

numbers_q = list()
operations_q = list()

oplist = list()
ops = ["+", "-", "x", "/", "xʸ", "√"]
for op in ops:
    oplist.append(tk.Button(
        master=frame_bot2,
        text=op,
        foreground="black",
        background="light grey",
        width=7,
        command=lambda op=op: (numbers_q.append(display['text']), operations_q.append(op), fs.Clr(display))
        ))
    oplist[-1].pack() 

button_equal = tk.Button(
    master=frame_bot2,
    text="=",
    foreground="black",
    background="light grey",
    width=7,
    height=2,
    command=lambda: (calculate(numbers_q, operations_q, display['text']))
    )
button_equal.pack()


button_clr = tk.Button(
    master=frame_bot2,
    text="Clear",
    foreground="black",
    background="light grey",
    width=7,
    command=lambda: full_clr(display, numbers_q, operations_q)
    )
button_clr.pack()

def full_clr(display, num_q, op_q):
    global numbers_q, operations_q
    display['text'] = 0    
    numbers_q = list()
    operations_q = list()

def calculate(num_q, op_q, num):
    global numbers_q, operations_q
    num_q.append(num)
    
    while len(op_q) > 0:
        if "√" in op_q:
            num_q[op_q.index("√")] = sqrt(float(num_q[op_q.index("√")+1]))
            num_q.pop(op_q.index("√")+1)
            op_q.pop(op_q.index("√"))
        elif "xʸ" in op_q:
            num_q[op_q.index("xʸ")] = float(num_q[op_q.index("xʸ")]) ** float(num_q[op_q.index("xʸ")+1])
            num_q.pop(op_q.index("xʸ")+1)
            op_q.pop(op_q.index("xʸ"))
        elif "x" in op_q:
            num_q[op_q.index("x")] = float(num_q[op_q.index("x")]) * float(num_q[op_q.index("x")+1])
            num_q.pop(op_q.index("x")+1)
            op_q.pop(op_q.index("x"))
        elif "/" in op_q:
            if not float(num_q[op_q.index("/")+1]) == 0:
                num_q[op_q.index("/")] = float(num_q[op_q.index("/")]) / float(num_q[op_q.index("/")+1])
                num_q.pop(op_q.index("/")+1)
                op_q.pop(op_q.index("/"))
            else:
                num_q[0] = "Math error"
                break
        elif "+" in op_q:
            num_q[op_q.index("+")] = float(num_q[op_q.index("+")]) + float(num_q[op_q.index("+")+1])
            num_q.pop(op_q.index("+")+1)
            op_q.pop(op_q.index("+"))
        elif "-" in op_q:
            num_q[op_q.index("-")] = float(num_q[op_q.index("-")]) - float(num_q[op_q.index("-")+1])
            num_q.pop(op_q.index("-")+1)
            op_q.pop(op_q.index("-"))

    display['text'] = num_q[0]
    numbers_q = list()
    operations_q = list()
    

window.mainloop()