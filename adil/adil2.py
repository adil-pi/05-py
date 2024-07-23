from tkinter import *


def switch_frame():
    if frame1.winfo_ismapped():
        frame1.pack_forget()
        frame2.pack(fill='both', expand=True)
    else:
        frame2.pack_forget()
        frame1.pack(fill='both', expand=True)


root = Tk()
root.title("Многооконное приложение")
root.geometry("400x400")

frame1 = Frame(root)
frame2 = Frame(root)

label1 = Label(frame1, text="Это первое окно")
label1.pack(padx=10, pady=10)

label2 = Label(frame2, text="Это второе окно")
label2.pack(padx=10, pady=10)

button = Button(root, text="Переключить окно", command=switch_frame)
button.pack()

frame1.pack(fill='both', expand=True)


root.mainloop()