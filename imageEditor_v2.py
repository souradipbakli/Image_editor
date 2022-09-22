from cgitb import text
from email.mime import image
from fileinput import filename
import tkinter as tk
from turtle import color
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from PIL import ImageEnhance
import cv2
import numpy as np

def displayImage(displayImage):
    ImagetoDisplay=displayImage.resize((900,600),Image.ANTIALIAS)
    ImagetoDisplay=ImageTk.PhotoImage(ImagetoDisplay)
    showWindow.config(image=ImagetoDisplay)
    showWindow.photo_ref=ImagetoDisplay
    showWindow.pack()

def importButton_callback():
    global originalImage
    filename=filedialog.askopenfilename()
    originalImage=Image.open(filename)
    displayImage(originalImage )

def saveButton_callback():
    savefile=filedialog.asksaveasfile(defaultextension=".JPEG")
    outputImage.save(savefile)

def closeButton_callback():
    window.destroy()

def brightness_callback(brightness_pos):
    brightness_pos=float(brightness_pos)

    print(brightness_pos)
    global outputImage
    enhancer=ImageEnhance.Brightness(originalImage)
    outputImage=enhancer.enhance(brightness_pos)
    displayImage(outputImage)

def contrast_callback(contrast_pos):
    contrast_pos=float(contrast_pos)
    print(contrast_pos)
    global outputImage
    enhancer=ImageEnhance.Contrast(originalImage)
    outputImage=enhancer.enhance(contrast_pos)
    displayImage(outputImage)

def yellowButton_callback():
    opencvImage=cv2.cvtColor(np.array(originalImage),cv2.COLOR_RGB2BGR)
    opencvImage[::0]=20
    global outputImage
    outputImage=Image.fromarray(cv2.cvtColor(opencvImage,cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def blueButton_callback():
    pass

def pinkButton_callback():
    pass

def orangeButton_callback():
    pass

def noneButton_callback():
    pass


window=tk.Tk()
# screen_width=window.winfo_screenmmwidth()
# screen_height=window.winfo_screenmmheight()
screen_width= window.winfo_screenwidth()               
screen_height= window.winfo_screenheight()

# window.geometry(f'{screen_width}x{screen_height}')
window.geometry("%dx%d" % (screen_width, screen_height))

Frame1=tk.Frame(window,height=20,width=200)
Frame1.pack(anchor=tk.N)

Frame2=tk.Frame(window,height=20,width=screen_width)
Frame2.pack(anchor=tk.NW)

Frame3=tk.Frame(window,height=20)
Frame3.pack(anchor=tk.N)

importButton=tk.Button(Frame1,text="Import",padx=10,pady=5,command=importButton_callback)
importButton.grid(row=0,column=0)

saveButton=tk.Button(Frame1,text="Save",padx=10,pady=5,command=saveButton_callback)
saveButton.grid(row=0,column=1)

closeButton=tk.Button(Frame1,text="Close",padx=10,pady=5,command=closeButton_callback)
closeButton.grid(row=0,column=2)

brightnessSlider=tk.Scale(Frame2,label="Brightness",from_=0,to=2,orient=tk.HORIZONTAL,length=screen_width,
                resolution=0.1,command=brightness_callback)
brightnessSlider.set(1)
brightnessSlider.pack(anchor=tk.N)

contrastSlider=tk.Scale(Frame2,label="Contrast",from_=0,to=2,orient=tk.HORIZONTAL,length=screen_width,
                command=contrast_callback,resolution=0.1)
contrastSlider.set(1)
contrastSlider.pack(anchor=tk.N)

yellowButton=tk.Radiobutton(Frame3,text="Yellow",width=30,value=1,command=yellowButton_callback)
yellowButton.grid(row=0,column=0)

blueButton=tk.Radiobutton(Frame3,text="Blue",width=30,value=2,command=blueButton_callback)
blueButton.grid(row=0,column=1)

pinkButton=tk.Radiobutton(Frame3,text="Pink",width=30,value=3,command=pinkButton_callback)
pinkButton.grid(row=0,column=2)

orangeButton=tk.Radiobutton(Frame3,text="Orange",width=30,value=4,command=orangeButton_callback)
orangeButton.grid(row=0,column=3)

noneButton=tk.Radiobutton(Frame3,text="None",width=30,value=5,command=noneButton_callback)
noneButton.grid(row=0,column=4)
noneButton.select()

showWindow=tk.Label(window)
showWindow.pack()
tk.mainloop()