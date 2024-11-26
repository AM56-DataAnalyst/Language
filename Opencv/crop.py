import cv2
import numpy as np


itc = cv2.imread("C:/Users/coolc/vs code/Opencv/Air-Force-One-president-use-Boeing-747.jpg")


"""def crop(event, x, y, flags, params):
    pass


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)

while True:

    cv2.imshow("window",itc)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()"""

###end

flag = False
ix = -1
iy = -1


def crop(event,x,y,flags,params):

    global flag,ix,iy

    if event == 1:

        flag = True
        ix = x
        iy = y

    elif event ==4:

        fx = x
        fy = y
        
        flag = False
        cv2.rectangle(itc,pt1 = (ix,iy), pt2 =(x,y), thickness=1,color=(0,0,0))

        # Crop tools
        cropped = itc[iy:fy,ix:fx]
        cv2.imwrite("cropped.png",cropped)

        cv2.imshow("new_window",cropped)

        cv2.waitkey(0)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)

while True:
    cv2.imshow("window",itc)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()