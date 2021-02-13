from PIL import ImageTk #sudo apt-get install python-imaging-tk
import matplotlib.pyplot as plt
from tkinter import filedialog
from cv2 import cv2 as cv
import matplotlib as mpl
import tensorflow as tf
from tkinter import *
import tkinter as tk
import numpy as np
import PIL.Image
import os


def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("png file","*.png"),("jpg file","*.jpg")))
    img = PIL.Image.open(fln)
    display = img.resize((350,350))
    display.thumbnail((350, 350))
    display = ImageTk.PhotoImage(display)
    lbl.configure(image=display)
    lbl.image = display
    img = img.resize((28,28))
    img.thumbnail((28, 28))

    import model

    img = cv.imread(fln)[:,:,0]
    img = np.invert(np.array([img]))
    prediction = model.model.predict(img)
    print(np.argmax(prediction))
    plt.show()


root = Tk()

frm = Frame(root)
frm.pack(side= BOTTOM, padx=15, pady=15)
lbl = Label(root)
lbl.pack()
btn = Button(frm, text="Image", command = showimage)
btn.pack(side=tk.LEFT, padx=10)
btn2= Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)

root.title("Digit Reccognition")
root.geometry("300x350")
root.mainloop()    