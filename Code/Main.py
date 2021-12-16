import cv2 as cv
import numpy as np
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk





colorObject =  [                               # h_min, s_min, v_min, h_max, s_max, v_max
            [61, 48, 25, 179, 255, 185],
            [94, 98, 0, 138, 149, 40],
            [111, 87, 0, 179, 255, 255],        # pen biru
            [86, 74, 0, 179, 74, 132]
            ]     

colorPoint = [                           # BGR
                [51,153,255],
                [237, 202, 147],
                [116, 113, 244],
                [116, 113, 244]
                ]              

points = []                               # x, y, colorId


def saveAsPicture():
    global imgResult, idAfter
    
    lblOriImg.after_cancel(idAfter)
    imgSave = opencv2Pill(imgResult)

    extension = [("JPG File", "*.jpg")]
    file = filedialog.asksaveasfile(filetypes = extension, defaultextension = extension)
    if file:
        imgSave.save(file)
        
    lblOriImg.after(1, videoStream)
    

def findColor(img, colorObject, colorPoint):
    global imgResult
    
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in colorObject:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)

        cv.circle(imgResult, (x,y), 10, colorPoint[count], cv.FILLED)
        if x != 0 & y != 0:
            newPoints.append([x,y,count])
        newPoints.append([x,y,count])
        count += 1
        # cv.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            # cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return x+w // 2, y


def drawOnCanvas(points, colorPoint):
    global imgResult
    
    for point in points:
        cv.circle(imgResult, (point[0], point[1]), 10, colorPoint[point[2]], cv.FILLED)


# def main():
#     while True:
#         sucess, img = cap.read()
#         imgResult = img.copy()
#         newPoints = findColor(img, colorObject, colorPoint)
#         if len(newPoints) != 0:
#             for newP in newPoints:              # Kita tidak bisa menaruh list ke list.
#                 # print(newP)
#                 points.append(newP)
#         if len(points) != 0:
#             drawOnCanvas(points, colorPoint)
        
#         cv.imshow("Result", imgResult)

#         if cv.waitKey(1) & 0xFF == ord('q'):
#             break   



def setResult(img):
    imgTk = ImageTk.PhotoImage(img)
    lblOriImg.configure(image=imgTk)
    lblOriImg.image = imgTk
    lblOriImg.pack()

def opencv2Pill(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgPill = Image.fromarray(img)
    return imgPill

def resizeImg(img, width, height):
    img = cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)
    return img


def videoStream():
    global cap, imgResult, idAfter
    
    sucess, img = cap.read()
    
    img = resizeImg(img, 852, 480)
    imgResult = img.copy()
    newPoints = findColor(img, colorObject, colorPoint)
    if len(newPoints) != 0:
        for newP in newPoints:              # Kita tidak bisa menaruh list ke list.
            print(newP)
            points.append(newP)
    if len(points) != 0:
        drawOnCanvas(points, colorPoint)
    
    setResult(opencv2Pill(imgResult))
    idAfter = lblOriImg.after(1, videoStream)
    


if __name__ == '__main__':
    
        
    style = Style()
    window = style.master


    frm = ttk.Frame(window, style='primary.TFrame')
    # frm.pack(side='top')
    frm.pack_propagate(0)
    frm.pack(fill=tk.BOTH, expand=1)

    # Size window : 852 x 480
    frmImgOri = ttk.Frame(frm, style='secondary.TFrame', width=852, height=480)
    frmImgOri.grid(row=0, column=0, padx=25, pady=25)


    frmBtn = ttk.Frame(frm, style='secondary.TFrame', width=852, height=150)
    frmBtn.grid(row=1, column=0, padx=25, pady=(10,50))

    lblOriImg = ttk.Label(frmImgOri)
    # lblOriImg.pack()


    btnCls = ttk.Button(frmBtn, text='Clear Canvas', style='success.TButton', cursor="hand2")
    btnCls.pack(side='left', padx=37, pady=10)

    btnSave = ttk.Button(frmBtn, text='Save as Picture', style='success.TButton', cursor="hand2",command=saveAsPicture)
    btnSave.pack(side='left', padx=37, pady=10)

    btnSetDraw = ttk.Button(frmBtn, text='Set Draw', style='success.TButton', cursor="hand2")
    btnSetDraw.pack(side='left', padx=37, pady=10)

    btnAddColor = ttk.Button(frmBtn, text='Add Color Detection', style='success.TButton', cursor="hand2")
    btnAddColor.pack(side='left', padx=37, pady=10)

    btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2", command=lambda: exit())
    btnExit.pack(side='left', padx=37, pady=10)

    cap = cv.VideoCapture(0)


    window.title("Virtual Paint")
    # window.geometry("1280x720")
    window.resizable(0, 0)
    window.after(1, videoStream)
    window.mainloop()

    
    # cap.set(3, frameWidth)            # Resize lebar dari frame
    # cap.set(4, frameHeight)           # Resize tinggi dari frame
    
