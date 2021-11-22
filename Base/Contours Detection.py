import cv2
import numpy as np


frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])

    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),  None, scale, scale)

                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0,0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)

            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        hor = np.hstack(imgArray)
        ver = hor

    return ver


def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))

            x, y, w, h = cv2.boundingRect(approx)
            
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x+w+20, y+45), cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
                

while True:
    success, img = cap.read()
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7,7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDil, imgContour)

    imgStack = stackImages(0.8, (
                                [img, imgGray, imgCanny],
                                [imgDil, imgContour, imgContour]
                                ))

    cv2.imshow("Result", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

                

'''
    NB :
        - cv2.GaussianBlur()    ~> Berfungsi untuk memblur gambar menggunakan filter Gaussian.
        - cv2.GaussianBlur(<sumber gambar yg telah dibaca>, (<kernel size sumbu x>, <kernel size sumbu y>), <ketebalan>)

        - cv2.COLOR_BGR2GRAY	~> Berfungsi untuk memberi warna abu-abu.

        - cv2.Canny()		    ~> Berfungsi untuk menemukan tepi / ujunng dalam gambar menggunakan algoritma Canny.
        - cv2.Canny(<sumber gambar yg telah dibaca>, <threshold1>, <threshold2>)

        - cv2.dilate()		    ~> Berfungsi untuk melebarkan gambar dengan menggunakan elemen penataan tertentu.
        - cv2.dilate(<sumber gambar yg telah dibaca>, <kernel / array penataan yang digunakan untuk dilatasi>, iterations=<berapa kali dilatasi diterapkan [int]>)

        - cv2.findContours()	~> Berfungsi untuk mencari kontur (garis bentuk) pada suatu gambar dan akan mereturn contours dan hierarchy dari gambar.

        - cv2.findContours(<sumber gambar yg telah dibaca>, <contours [OutputArrayOfArrays]>, <hierarchy [OutputArray]>)

        - cv2.RETR_EXTERNAL	    ~> Berfungsi untuk mengambil kontur luar yang ekstrem.
            - hierarchy[i][2]=hierarchy[i][3]=-1

        - cv2.CHAIN_APPROX_NONE	~> Berfungsi untuk benar-benar menyimpan semua titik kontur.
            - Artinya, setiap 2 titik berikutnya (x1,y1) dan (x2,y2) dari kontur akan menjadi tetangga horizontal, vertikal atau diagonal, yaitu, max(abs(x1-x2),abs(y2-y1)) == 1.

        - cv2.drawContours()	~> Berfungsi untuk menggambar garis kontur.
        - cv2.drawContours(<sumber gambar yg akan digambari garis>, <contours>, <contourIdx>, <warna>, <ketebalan>)
            - contours		    -> Semua kontur input. Setiap kontur disimpan sebagai vektor titik.
            - contourIdx	    -> Parameter yang menunjukkan kontur untuk menggambar. Jika negatif, semua kontur digambar.
            - color		        -> (r, g, b)

        - .copy()			    ~> Berfungsi untuk mengcopy suatu gambar.
        - <gambar yg ingin dicopy>.copy()

        - cv2.contourArea()	    ~> Berfungsi untuk menghitung luas suatu kontur.
        - cv2.contourArea(<contour yg ingin dihitung luasnya>)

        - cv2.arcLength()		~> Berfungsi untuk menghitung keliling kontur dari panjang kurva.
        - cv2.arcLength(<contour yg ingin dihitung kelilingnya>, <closed or not [bool]>)
            - closed	-> Menunjukkan apakah kurva ditutup atau tidak.

        - cv2.approxPolyDP()	~> Berfungsi untuk mendekati kurva poligonal dengan presisi yang ditentukan.
        - cv2.approxPolyDP(<contour / curve>, <approxCurve>, <closed or not [bool]>)
            - approxCurve	    -> Hasil perkiraan. Jenisnya harus sesuai dengan jenis kurva input.
            - closed		    -> Jika True, kurva yang didekati ditutup (simpul pertama dan terakhirnya terhubung). Jika False, itu tidak ditutup.

        - cv2.boundingRect()    ~> Berfungsi untuk mengembalikan persegi panjang integer atas - kanan, minimal yang berisi persegi panjang yang diputar
        - cv2.boundingRect(<array>)

        - cv2.rectangle()		~> Berfungsi untuk menggambar persegi panjang atas - kanan yang sederhana, tebal, atau filled pada suatu gambar.
        - cv2.rectangle(<sumber gambar>, <point 1>, <point 2>, <warna>, <ketebalan>)
            - point 1	        -> Titik sudut persegi panjang.
            - point 2	        -> Titik sudut persegi panjang yang berlawanan dengan point 1.
            - color	            -> (r, g, b)

        - cv2.putText()	        ~> Berfungsi untuk menggambar string teks pada suatu gambar.
        - cv2.putText(<sumber gambar>, <teks [string]>, <posisi>, <jenis font>, <ukuran font>, <warna teks>, <ketebalan>)
            - posisi	        -> Sudut kiri bawah string teks pada gambar.
            - color	            -> (r, g, b)


'''
                
                
                
                
                
                

