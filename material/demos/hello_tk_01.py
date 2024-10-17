import tkinter as tk
import tkinter.messagebox as mb

window = tk.Tk()
anwser = mb.askyesno(title="Confirmer?", message="Voulez-vous quitter ?")

window.mainloop()
