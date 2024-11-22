import tkinter as tk
# ttk will contain our widgets
from tkinter import ttk

window = tk.Tk()
window.geometry("600x300")


label = ttk.Label(window, text="Hello World")
label2 = ttk.Label(window, text="Other text")

def print_message():
    label.config(text="The button has been pressed")
    print("button pressed")
button = ttk.Button(window, text="Click Me", command=print_message)

# Change the order of pack and see what happens
label2.grid(row=0, column=0)
label.grid(row=0, column=1)
button.grid(row=1, column=0)

window.mainloop()