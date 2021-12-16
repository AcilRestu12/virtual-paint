import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import cv2
import numpy as np

# --- functions ---

def savefile():
    # filename = filedialog.asksaveasfile(mode='w', defaultextension=(
    #                                     ("All Files", "*.*",),
    #                                     ("PNG File", "*.png"), 
    #                                     ("JPG File", "*.jpg")),
    #                                     filetypes=(
    #                                     ("All Files", "*.*",),
    #                                     ("PNG File", "*.png"), 
    #                                     ("JPG File", "*.jpg"))
    #                                 )
    # if not filename:
    #     return
    
    extension = [("JPG File", "*.jpg")]
    file = filedialog.asksaveasfile(filetypes = extension, defaultextension = extension)
    
    # ekstension = filename.split('.')[-1]
    
    # print(filename.get()
    
    print(f'File Name : {file}\n')
    # print(f'ekstension : {ekstension}\n')
    
    if file:
        edge.save(file)

# --- main ---

root = tk.Tk()

img = cv2.imread('Test\Resource\lena.png')
edge = Image.fromarray(img)

tk_edge = ImageTk.PhotoImage(edge)
label = tk.Label(root, image=tk_edge)
label.pack()

button = tk.Button(root, text="save as", command=savefile)
button.pack()

root.mainloop()