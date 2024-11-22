import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x300")

"""Create a tkinter app that shows an a label and a button
The label shows 0 initially and is incremented after each click on the button"""
i = 0
label = ttk.Label(window, text=str(i))

def increment():
    # tells python to use the global i defined at line 9 and not create a new local variable i
    global i  
    i += 1
    label.config(text= str(i))
    
button = ttk.Button(window, text="Exercice 1", command=increment)
label.pack()
button.pack()

# method 2
label_1_method2 = ttk.Label(window, text=str(i))

def increment_1_method2():
    # get the value of the label, convert it to int and increment it
    i = int(label.cget("text"))
    label_1_method2.config(text= str(i+1))
    
button_1_method2 = ttk.Button(window, text="Exercice 1", command=increment_1_method2)
label_1_method2.pack()
button_1_method2.pack()

"""Create a tkinter app that shows two labels and a button
The labels show 0 initially. When we click on the button the first time, the first label
increments, when we click on the button a second time, the second label increments.
When we click on the button a third time, the first label increments and so on"""

"""Create a tinkter app that shows a button on top and a label below it.
When we click on the button, the labal adds a new line with the text "line {i}".
For example, if we click on the button 4 times, then the label shows:
line 1
line 2
line 3
line 4
"""
window.mainloop()