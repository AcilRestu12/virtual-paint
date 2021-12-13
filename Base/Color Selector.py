from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()
root.title("Pilihan Warna")
warna = "light blue"
root.config(bg=warna)


# Fungsi Warna

def pilih():
    global warna

    hasil = askcolor(title="Pilih Warnanya")
    RGB, HEX = hasil
    warna = HEX

    print(f'Warna RGB : {RGB}')
    print(f'Warna HEX : {HEX}\n')
    root.config(bg=warna)
    

# Button

b1 = Button(root, text="Pilih Warna", fg="darkgreen", bd=5, font="Times 20 bold", relief=RIDGE, command=pilih)
b1.pack(padx=75, pady=40)

root.mainloop()



'''
    NB :
        - askcolor()	~> Berfungsi untuk mengambil suatu warna dengan gui.
        - <variabel hasil> = askcolor(title="<judul header">)
        - RGB, HEX = <variabel hasil>




'''

