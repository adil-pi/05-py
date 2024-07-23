from tkinter import *
import random


def play_game():
    user = entry.get()
    if user != "":
        user = int(user)
        rand = random.randint(1, 100)
        if rand == user:
            txt["text"] = "Вы победили!"
        elif rand < user: 
            txt["text"] = "Загаданое число меньше!"
        elif rand > user: 
            txt["text"] = "Загаданое число больше!"
        
        
root = Tk()
root.title("Угадай число")
root.geometry("500x300")

frame = Frame(root)
frame.pack(anchor="center")

lab1 = Label(frame, text="Угадай число от 1 до 100", font=('Comic Sans MS', 12))
lab1.pack()

entry = Entry(frame, font=('Comic Sans MS', 12))
entry.pack()

btn = Button(frame, text="готово", font=('Comic Sans MS', 12), bg="#05f5d5", fg="#fa020b", command=play_game)
btn.pack()

txt = Label(frame, text="")
txt.pack()

root.mainloop()