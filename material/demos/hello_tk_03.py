from tkinter import *

window = Tk()
window.geometry("600x300")

entered_text = StringVar()
textbox = Entry(window, textvariable=entered_text)
textbox.pack()


def run_prompt():
    print("prompt saisi", entered_text.get())
    print("prompt saisi", textbox.get())
    response = f"Réponse à la main pour le prompt {entered_text.get()}. A remplacer par une vraie réponse"
    print("réponse", response)


def reset_entry():
    entered_text.set("")


run_button = Button(window, text="Run", command=run_prompt)
run_button.pack()

clear_button = Button(window, text="Clear", command=reset_entry)
clear_button.pack()

window.mainloop()
