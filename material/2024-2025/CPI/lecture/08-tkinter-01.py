import tkinter as tk
# ttk will contain our widgets
from tkinter import ttk

window = tk.Tk()
window.geometry("600x300")

def print_message():
    print("button pressed")

label = ttk.Label(window, text="Hello World")
label2 = ttk.Label(window, text="Other text")
button = ttk.Button(window, text="Click Me", command=print_message)

# Change the order of pack and see what happens
label2.pack()
label.pack()
button.pack()

window.mainloop()