from tkinter import *
from datetime import datetime


prompts = []

window = Tk()
window.geometry("600x300")

entered_text = StringVar()
history_content = StringVar()
textbox = Entry(window, textvariable=entered_text)
textbox.pack()


def run_prompt():
    print("prompt saisi", entered_text.get())
    print("prompt saisi", textbox.get())
    response = f"Réponse à la main pour le prompt {entered_text.get()}. A remplacer par une vraie réponse"
    print("réponse", response)
    prompt = {
        "query": entered_text.get(),
        "response": response,
        "date": datetime.now(),
    }
    prompts.append(prompt)
    print(prompts)
    temp_history_content = ""
    for prompt in prompts:
        temp_history_content += f"query: {prompt['query']} \n"
        temp_history_content += f"responst: {prompt['response']} \n"
        temp_history_content += f"date: {prompt['date']} \n"
        temp_history_content += f"\n--------------\n"
    history_content.set(temp_history_content)


def reset_entry():
    entered_text.set("")


run_button = Button(window, text="Run", command=run_prompt)
run_button.pack()

clear_button = Button(window, text="Clear", command=reset_entry)
clear_button.pack()

history = Label(window, textvariable=history_content)
history.pack()

window.mainloop()
