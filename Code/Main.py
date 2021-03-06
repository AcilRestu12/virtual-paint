import cv2 as cv
import numpy as np



frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
# cap.set(3, frameWidth)            # Resize lebar dari frame
# cap.set(4, frameHeight)           # Resize tinggi dari frame


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


def findColor(img, colorObject, colorPoint):
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
        # newPoints.append([x,y,count])
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
    for point in points:
        cv.circle(imgResult, (point[0], point[1]), 10, colorPoint[point[2]], cv.FILLED)


if __name__ == '__main__':
    while True:
        sucess, img = cap.read()
        imgResult = img.copy()
        newPoints = findColor(img, colorObject, colorPoint)
        if len(newPoints) != 0:
            for newP in newPoints:              # Kita tidak bisa menaruh list ke list.
                # print(newP)
                points.append(newP)
        if len(points) != 0:
            drawOnCanvas(points, colorPoint)
        
        cv.imshow("Result", imgResult)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break   

    cap.release()
    cv.destroyAllWindows()