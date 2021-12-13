import cv2
import numpy as np
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

import AddObject



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



window.title("Virtual Paint")
# window.geometry("1280x720")
window.resizable(0, 0)
window.mainloop()


