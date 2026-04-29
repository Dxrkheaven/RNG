from tkinter import *
import random
import string

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

window = Tk()
window.geometry("400x200")
window.resizable(FALSE, FALSE)

def gen():
    r = random.choice(list)
    global randomnum
    randomnum = "".join(random.choice(string.digits) for i in range(r))
    label.config(text=randomnum)

def save():
    with open("numbers.txt", "a") as file:
        file.write(f"number = {randomnum}\n")

def doall():
    gen()
    save()

def search():
    target = entry.get()

    with open("numbers.txt", "r") as file:
        content = file.read()

        if f"number = {target}" in content:
            result.config(text="Found")
        else:
            result.config(text="Not Found")

label = Label(window, text="-")
b1 = Button(window, text="Generate Number", command=doall)

entry = Entry(window)
b2 = Button(window, text="Search Number", command=search)

result = Label(window, text="-")

label.pack()
b1.pack(pady = 5)

entry.pack(pady = 5)
b2.pack()
result.pack()

window.mainloop()