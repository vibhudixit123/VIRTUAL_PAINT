import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0 )
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

#myColors = [[5,107,0,19,255,255],  #orange_color
myColors = [[133,56,0,159,156,255], #purpel_color
            [57,76,0,100,255,255],  #green_color
            [90,48,0,118,255,255]] #blue_color



#mycolorvalue = [[51,153,255],
mycolorvalue = [[255,0,255],
                [0,255,0],
                [255,0,0]]

myPoints = []

#function_to_take_input_from_myColor_array:

def findcolor(img,myColors,mycolorvalue):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newpoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV,lower,upper)
        x, y = getContours(mask)
        cv.circle(imgresult,(x,y),10,mycolorvalue[count],cv.FILLED)
        if x!=0 and y!=0:
            newpoints.append([x,y,count])
        count += 1

    return newpoints

#function_get_contour:

def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area= cv.contourArea(cnt)

        if area>500:
            cv.drawContours(imgresult,cnt,-1,(255, 0, 0),3)
            peri= cv.arcLength(cnt,True)

            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv.boundingRect(approx)
    return x+w//2,y


#function_to_draw_canvas:

def drawoncanvas(myPoints,mycolorvalue):
    for point in myPoints:
        cv.circle(imgresult, (point[0],point[1]),10,mycolorvalue[point[2]], cv.FILLED)


#all_outputs:

while True:
    ret, img = cap.read()
    imgresult = img.copy()
    newpoints = findcolor(img, myColors,mycolorvalue)

    if len(newpoints)!=0:
       for newp in newpoints:
           myPoints.append(newp)
    if len(myPoints)!=0:
        drawoncanvas(myPoints, mycolorvalue)
    cv.imshow('Video', imgresult)
    if cv.waitKey(1) == ord('q'):
        break


