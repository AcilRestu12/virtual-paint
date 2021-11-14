import cv2
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
# Create a frame
app = Frame(root, bg="white")
app.grid()
# Create a label in the frame
lmain = Label(app)
lmain.grid()
# Capture from camera
cap = cv2.VideoCapture(0)
def video_stream():
    _, frame = cap.read()
    print(frame)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)
root.after(1, video_stream)
root.mainloop()