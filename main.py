from PIL import ImageTk #sudo apt-get install python-imaging-tk
import matplotlib.pyplot as plt
from tkinter import filedialog
import tensorflow as tf
from tkinter import *
import tkinter as tk
import numpy as np
import PIL.Image
import cv2 as cv
import os


def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("png file","*.png"),("jpg file","*.jpg")))
    img = PIL.Image.open(fln)
    copy = img.resize((350,350))
    copy.thumbnail((350, 350))
    copy = ImageTk.PhotoImage(copy)
    lbl.configure(image=copy)
    lbl.image = copy

    import model


    img = np.invert(img)
    prediction = model.predict(tf.argmax(prediction))
    print ("Prediction for test image:", np.squeeze(prediction))

    '''
    if img.endswith('.png','.jpg'):
        img = np.invert(img)
        prediction = model.predict(img)
        print(np.argmax(prediction))

        notification = Label(root, img[0])
        notification.pack() 
'''


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