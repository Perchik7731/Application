import tkinter as tk

def on_button_click():
    label.config(text="Кнопка нажата")

root = tk.Tk()
root.title("Билеты на концерт Кати Самбуки")
root.geometry("500x500")

label = tk.Label(root, text="Нажми на кнопку", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Нажми на меня", command=on_button_click)
button.pack(pady=10)

root.mainloop()