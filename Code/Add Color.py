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


def videoStream():
    global cap
    
    sucess, img = cap.read()
    imgCV = cv.cvtColor(img, cv.COLOR_BGR2RGBA)
    imgCV = resizeImg(imgCV, 852, 480)
    imgPill = Image.fromarray(imgCV)
    imgtk = ImageTk.PhotoImage(image=imgPill)
    
    
    lblImgRes.imgtk = imgtk
    lblImgRes.configure(image=imgtk)
    lblImgRes.pack()
    lblImgRes.after(1, videoStream)



if __name__ == '__main__':
    
    style = Style()
    window = style.master

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

    btnMask = ttk.Button(frmBtn, text='Mask', style='success.TButton', cursor="hand2", width=12)
    btnMask.pack(side='top', padx=33, pady=33)

    btnHSV = ttk.Button(frmBtn, text='HSV', style='success.TButton', cursor="hand2", width=12)
    btnHSV.pack(side='top', padx=33, pady=33)

    btnResult = ttk.Button(frmBtn, text='Result', style='success.TButton', cursor="hand2", width=12)
    btnResult.pack(side='top', padx=33, pady=33)

    btnAddColor = ttk.Button(frmBtn, text='Add Color', style='success.TButton', cursor="hand2", width=12)
    btnAddColor.pack(side='top', padx=33, pady=33)

    btnExit = ttk.Button(frmBtn, text='Back', style='danger.TButton', cursor="hand2", width=12)
    btnExit.pack(side='top', padx=33, pady=33)


    # Slider

    sldHueMin = ttk.Scale(frmSliderMin, from_=0, to=179, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255)
    lblHueMin = ttk.Label(frmSliderMin, text=f'HUE Min : {sldHueMin.get()}', style='info.Inverse.TLabel')
    lblHueMin.grid(row=0, column=0, padx=20, pady=10)
    sldHueMin.grid(row=0, column=1, padx=20, pady=10)

    sldSatMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255)
    lblSatMin = ttk.Label(frmSliderMin, text=f'SAT Min : {sldSatMin.get()}', style='info.Inverse.TLabel')
    lblSatMin.grid(row=1, column=0, padx=20, pady=10)
    sldSatMin.grid(row=1, column=1, padx=20, pady=10)

    sldValueMin = ttk.Scale(frmSliderMin, from_=0, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=255)
    lblValueMin = ttk.Label(frmSliderMin, text=f'VALUE Min : {sldValueMin.get()}', style='info.Inverse.TLabel')
    lblValueMin.grid(row=2, column=0, padx=20, pady=10)
    sldValueMin.grid(row=2, column=1, padx=20, pady=10)

    sldHueMax = ttk.Scale(frmSliderMax, from_=0, to=179, value=179, orient='horizontal', style='info.Horizontal.TScale', length=255)
    lblHueMax = ttk.Label(frmSliderMax, text=f'HUE Max : {sldHueMax.get()}', style='info.Inverse.TLabel')
    lblHueMax.grid(row=0, column=0, padx=20, pady=10)
    sldHueMax.grid(row=0, column=1, padx=20, pady=10)

    sldSatMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=255)
    lblSatMax = ttk.Label(frmSliderMax, text=f'SAT Max : {sldSatMax.get()}', style='info.Inverse.TLabel')
    lblSatMax.grid(row=1, column=0, padx=20, pady=10)
    sldSatMax.grid(row=1, column=1, padx=20, pady=10)

    sldValueMax = ttk.Scale(frmSliderMax, from_=0, to=255, value=255, orient='horizontal', style='info.Horizontal.TScale', length=255)
    lblValueMax = ttk.Label(frmSliderMax, text=f'VALUE Max : {sldValueMax.get()}', style='info.Inverse.TLabel')
    lblValueMax.grid(row=2, column=0, padx=20, pady=10)
    sldValueMax.grid(row=2, column=1, padx=20, pady=10)



    window.title("Virtual Paint")
    # window.geometry("1280x720")
    # window.resizable(0, 0)
    window.after(1, videoStream)
    window.mainloop()


