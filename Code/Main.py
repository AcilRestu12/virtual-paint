import cv2 as cv
import numpy as np
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk





colorObject =  [                               # h_min, s_min, v_min, h_max, s_max, v_max
            [61, 48, 25, 179, 255, 185],
            [94, 98, 0, 138, 149, 40],
            [111, 87, 0, 179, 255, 255]        # pen biru
            ]     

colorPoint = [                           # BGR
                [51,153,255],
                [237, 202, 147],
                [116, 113, 244]
                ]              

points = []                               # x, y, colorId


# def findColor(img, colorObject, colorPoint):
#     imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#     count = 0
#     newPoints = []
#     for color in colorObject:
#         lower = np.array(color[0:3])
#         upper = np.array(color[3:6])
#         mask = cv.inRange(imgHSV, lower, upper)
#         x, y = getContours(mask)

#         cv.circle(imgResult, (x,y), 10, colorPoint[count], cv.FILLED)
#         if x != 0 & y != 0:
#             newPoints.append([x,y,count])
#         # newPoints.append([x,y,count])
#         count += 1
#         # cv.imshow(str(color[0]), mask)
#     return newPoints


# def getContours(img):
#     contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#     x,y,w,h = 0,0,0,0
#     for cnt in contours:
#         area = cv.contourArea(cnt)
#         if area > 500:
#             # cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
#             peri = cv.arcLength(cnt, True)
#             approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
#             x, y, w, h = cv.boundingRect(approx)
#     return x+w // 2, y


# def drawOnCanvas(points, colorPoint):
#     for point in points:
#         cv.circle(imgResult, (point[0], point[1]), 10, colorPoint[point[2]], cv.FILLED)


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



def setOriginal(img):
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
    global cap
    sucess, img = cap.read()
    imgCV = cv.cvtColor(img, cv.COLOR_BGR2RGBA)
    imgCV = resizeImg(imgCV, 852, 480)
    imgPill = Image.fromarray(imgCV)
    imgtk = ImageTk.PhotoImage(image=imgPill)
    lblOriImg.imgtk = imgtk
    lblOriImg.configure(image=imgtk)
    lblOriImg.pack()
    lblOriImg.after(1, videoStream)
    


if __name__ == '__main__':
    
        
    style = Style()
    window = style.master


    frm = ttk.Frame(window, style='primary.TFrame')
    # frm.pack(side='top')
    frm.pack_propagate(0)
    frm.pack(fill=tk.BOTH, expand=1)

    # Size window : 852 x 480
    frmImgOri = ttk.Frame(frm, style='secondary.TFrame', width=852, height=480)
    # frmImgOri.pack_propagate(0)
    frmImgOri.grid(row=0, column=0, padx=25, pady=25)


    frmBtn = ttk.Frame(frm, style='secondary.TFrame', width=852, height=150)
    # frmBtn.pack_propagate(0)
    # frmBtn.pack(side="left", padx=20, pady=30)
    frmBtn.grid(row=1, column=0, padx=25, pady=(10,50))

    lblOriImg = ttk.Label(frmImgOri)
    # lblOriImg.pack()


    btnCls = ttk.Button(frmBtn, text='Clear Canvas', style='success.TButton', cursor="hand2")
    # btnCls.grid(row=2, column=0, padx=5, pady=10)
    btnCls.pack(side='left', padx=37, pady=10)

    btnSave = ttk.Button(frmBtn, text='Save as Picture', style='success.TButton', cursor="hand2")
    # btnSave.grid(row=2, column=0, padx=5, pady=10)
    btnSave.pack(side='left', padx=37, pady=10)

    btnSetDraw = ttk.Button(frmBtn, text='Set Draw', style='success.TButton', cursor="hand2")
    # btnSetDraw.grid(row=2, column=0, padx=5, pady=10)
    btnSetDraw.pack(side='left', padx=37, pady=10)

    btnAddColor = ttk.Button(frmBtn, text='Add Color Detection', style='success.TButton', cursor="hand2")
    # btnAddColor.grid(row=2, column=0, padx=5, pady=10)
    btnAddColor.pack(side='left', padx=37, pady=10)

    btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2")
    # btnExit.grid(row=0, column=2, columnspan=2, padx=20)
    btnExit.pack(side='left', padx=37, pady=10)

    cap = cv.VideoCapture(0)


    window.title("Virtual Paint")
    # window.geometry("1280x720")
    window.resizable(0, 0)
    window.after(1, videoStream)
    window.mainloop()

    
    # cap.set(3, frameWidth)            # Resize lebar dari frame
    # cap.set(4, frameHeight)           # Resize tinggi dari frame
    
