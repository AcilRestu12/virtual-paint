import cv2 as cv
import numpy as np
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk



    
def resizeImg(img, width, height):
    img = cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)
    return img

def ori():
    pass

def hsv(img):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    return imgHSV

def mask(img):
    hueMin = int(sldHueMin.get())
    satMin = int(sldSatMin.get())
    valueMin = int(sldValueMin.get())
    hueMax = int(sldHueMax.get())
    satMax = int(sldSatMax.get())
    valueMax = int(sldValueMax.get())
    
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([hueMin, satMin, valueMin])
    upper = np.array([hueMax, satMax, valueMax])
    mask = cv.inRange(imgHSV, lower, upper)
    
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    return mask

def result(img):
    hueMin = int(sldHueMin.get())
    satMin = int(sldSatMin.get())
    valueMin = int(sldValueMin.get())
    hueMax = int(sldHueMax.get())
    satMax = int(sldSatMax.get())
    valueMax = int(sldValueMax.get())
    
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([hueMin, satMin, valueMin])
    upper = np.array([hueMax, satMax, valueMax])
    mask = cv.inRange(imgHSV, lower, upper)
    
    result = cv.bitwise_and(img, img, mask = mask)
    return result


def setMaskOn():
    global maskOn, hsvOn, resultOn
    
    maskOn = True
    hsvOn, resultOn = False, False
    
    print(f'\nMask : {maskOn}')
    

    
def setHsvOn():
    global maskOn, hsvOn, resultOn
    
    hsvOn = True
    maskOn, resultOn = False, False
    
    print(f'\nHSV : {hsvOn}')
    
    
    
def setResultOn():
    global maskOn, hsvOn, resultOn
    
    resultOn = True
    maskOn, hsvOn = False, False
    
    print(f'\nResult : {resultOn}')
    


def videoStream():
    global cap, maskOn, hsvOn, resultOn
    
    sucess, img = cap.read()
    imgCV = cv.cvtColor(img, cv.COLOR_BGR2RGBA)

    if hsvOn:
        imgCV = hsv(imgCV)
        print('\nHSV On')
    elif maskOn:
        imgCV = mask(imgCV)
        print("\nMask On")
    elif resultOn:
        imgCV = result(imgCV)
        print("\nResult On")
    else:
        print("\nOriginal On")
        pass
    
    imgCV = resizeImg(imgCV, 852, 480)
    imgPill = Image.fromarray(imgCV)
    imgtk = ImageTk.PhotoImage(image=imgPill)
    
    
    lblImgRes.imgtk = imgtk
    lblImgRes.configure(image=imgtk)
    lblImgRes.pack()
    lblImgRes.after(1, videoStream)


def sldMove(e):
    hueMin = int(sldHueMin.get())
    satMin = int(sldSatMin.get())
    valueMin = int(sldValueMin.get())
    hueMax = int(sldHueMax.get())
    satMax = int(sldSatMax.get())
    valueMax = int(sldValueMax.get())
    
    lblHueMin.configure(text=f'HUE Min : {hueMin}')
    lblSatMin.configure(text=f'SAT Min : {satMin}')
    lblValueMin.configure(text=f'VALUE Min : {valueMin}')
    lblHueMax.configure(text=f'HUE Max : {hueMax}')
    lblSatMax.configure(text=f'SAT Max : {satMax}')
    lblValueMax.configure(text=f'VALUE Max : {valueMax}')


if __name__ == '__main__':
    
    style = Style()
    window = style.master
    
    hsvOn, maskOn, resultOn = False, False, False

    cap = cv.VideoCapture(0)

    
    frm = ttk.Frame(window, style='primary.TFrame')
    # frm.pack(side='top')
    frm.pack_propagate(0)
    frm.pack(fill=tk.BOTH, expand=1)

    # Size window : 852 x 480


    # Frame

    frmBtn = ttk.Frame(frm, style='secondary.TFrame', width=100, height=480)
    frmBtn.grid(row=0, column=0, padx=(50,25), pady=25)

    frmResult = ttk.Frame(frm, style='secondary.TFrame', width=852, height=480)
    frmResult.grid(row=0, column=1, padx=(25,50), pady=25)

    frmSlider = ttk.Frame(frm, style='secondary.TFrame', width=1055, height=150)
    frmSlider.grid(row=1, column=0, columnspan=2, padx=50, pady=(20,50))

    frmSliderMin = ttk.Frame(frmSlider, style='info.TFrame', width=500, height=150)
    frmSliderMin.grid(row=0, column=0, padx=15, pady=15)

    frmSliderMax = ttk.Frame(frmSlider, style='info.TFrame', width=500, height=150)
    frmSliderMax.grid(row=0, column=1, padx=15, pady=15)


    lblImgRes = ttk.Label(frmResult)
    # lblImgRes.pack()


    # Button

    btnMask = ttk.Button(frmBtn, text='Mask', style='success.TButton', cursor="hand2", width=12, command=setMaskOn)
    btnMask.pack(side='top', padx=33, pady=33)

    btnHSV = ttk.Button(frmBtn, text='HSV', style='success.TButton', cursor="hand2", width=12, command=setHsvOn)
    btnHSV.pack(side='top', padx=33, pady=33)

    btnResult = ttk.Button(frmBtn, text='Result', style='success.TButton', cursor="hand2", width=12, command=setResultOn)
    btnResult.pack(side='top', padx=33, pady=33)

    btnAddObject = ttk.Button(frmBtn, text='Add Object', style='success.TButton', cursor="hand2", width=12)
    btnAddObject.pack(side='top', padx=33, pady=33)

    btnExit = ttk.Button(frmBtn, text='Back', style='danger.TButton', cursor="hand2", width=12)
    btnExit.pack(side='top', padx=33, pady=33)


    # Slider

    sldHueMin = ttk.Scale(frmSliderMin, from_=0, to=179, value=0, orient='horizontal', style='info.Horizontal.TScale', length=256, command=sldMove)
    lblHueMin = ttk.Label(frmSliderMin, text=f'HUE Min : {sldHueMin.get()}', style='info.Inverse.TLabel', width=15)
    lblHueMin.grid(row=0, column=0, padx=20, pady=10)
    sldHueMin.grid(row=0, column=1, padx=20, pady=10)

    sldSatMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=256, command=sldMove)
    lblSatMin = ttk.Label(frmSliderMin, text=f'SAT Min : {sldSatMin.get()}', style='info.Inverse.TLabel', width=15)
    lblSatMin.grid(row=1, column=0, padx=20, pady=10)
    sldSatMin.grid(row=1, column=1, padx=20, pady=10)

    sldValueMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=256, command=sldMove)
    lblValueMin = ttk.Label(frmSliderMin, text=f'VALUE Min : {sldValueMin.get()}', style='info.Inverse.TLabel', width=15)
    lblValueMin.grid(row=2, column=0, padx=20, pady=10)
    sldValueMin.grid(row=2, column=1, padx=20, pady=10)

    sldHueMax = ttk.Scale(frmSliderMax, from_=0, to=179, value=179, orient='horizontal', style='info.Horizontal.TScale', length=256, command=sldMove)
    lblHueMax = ttk.Label(frmSliderMax, text=f'HUE Max : {sldHueMax.get()}', style='info.Inverse.TLabel', width=15)
    lblHueMax.grid(row=0, column=0, padx=20, pady=10)
    sldHueMax.grid(row=0, column=1, padx=20, pady=10)

    sldSatMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=256, command=sldMove)
    lblSatMax = ttk.Label(frmSliderMax, text=f'SAT Max : {sldSatMax.get()}', style='info.Inverse.TLabel', width=15)
    lblSatMax.grid(row=1, column=0, padx=20, pady=10)
    sldSatMax.grid(row=1, column=1, padx=20, pady=10)

    sldValueMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=256, command=sldMove)
    lblValueMax = ttk.Label(frmSliderMax, text=f'VALUE Max : {sldValueMax.get()}', style='info.Inverse.TLabel', width=15)
    lblValueMax.grid(row=2, column=0, padx=20, pady=10)
    sldValueMax.grid(row=2, column=1, padx=20, pady=10)



    window.title("Virtual Paint")
    # window.geometry("1280x720")
    window.resizable(0, 0)
    window.after(1, videoStream)
    window.mainloop()


