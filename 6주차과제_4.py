##2021041021 곽민정
##이미지 확대 축소
from tkinter import *
from tkinter.filedialog import *


def keyUp(event) :
    photo = PhotoImage(file = filename)
    photo = photo.zoom(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo


def keyDown(event) :
    photo = PhotoImage(file = filename)
    photo = photo.subsample(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo


window = Tk()
window.geometry("500x500")
window.title("이미지 확대 축소")

filename = "C:/Users/alswj/Desktop/g2.gif"

photo = PhotoImage(file = filename)
pLabel = Label(window, image = photo)
pLabel.pack()

window.bind("<Up>", keyUp)
window.bind("<Down>", keyDown)
window.mainloop()
