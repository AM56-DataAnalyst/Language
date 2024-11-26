import cv2
import numpy as np

img = cv2.imread("C:/Users/coolc/vs code/Opencv/image.png")

new_size = (512,512)
img = cv2.resize(img, new_size)
print(img.shape)

#cv2.imshow("window",img)
#cv2.waitKey(0)

# Convert RGB image to grey scale image
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow("window",grey_img)
#cv2.waitKey(0)

imgBlue = img[:,:,0] #Blue =0
#cv2.imshow("window",img)

imgGreen = img[:,:,1] #Green=0
#cv2.imshow("window",img)

imgRed = img[:,:,2] #Red = 0
#cv2.imshow("window",img)

new_img = np.hstack((imgBlue,imgGreen, imgRed))
#cv2.imshow("window",new_img)
#cv2.waitKey(0)

"""img_resize = cv2.resize(img, (img.shape[1]//2,img.shape[0]//2))
cv2.imshow("window",img_resize)
cv2.waitKey(0)

print(img_resize.shape)"""

#img_flip = cv2.flip(img,-1)

img_crop = img[0:300,0:300]

cv2.imwrite('fruits_small.png',img_crop)

#cv2.imshow("window",img_crop)
#cv2.waitKey(0)

"""ing = np.zeros((512,512,3))

#Rectangle
cv2.rectangle(ing,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)

#Circle
cv2.circle(ing,center=(100,400),radius=50,color=(0,0,255),thickness=3)

#Line
cv2.line(ing,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))

#Text
cv2.putText(ing,org=(100,100), fontScale=4,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text="Hello", fontFace=cv2.FONT_HERSHEY_TRIPLEX)

cv2.imshow("window",ing)
cv2.waitKey(0)"""

"""def draw(event,x,y,flags,params):
    if event ==4:
        cv2.circle(ibg,center=(x,y), radius=50,color=(255,0,255),thickness=2)
    #pass

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)

ibg = np.zeros((512,512,3))

while True:
    cv2.imshow("window",ibg)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()"""

flag = False
ix = -1
iy = -1


def draw(event,x,y,flags,params):

    global flag,ix,iy

    if event == 1:

        flag = True
        ix = x
        iy = y

    elif event ==0:

        if flag == True:
            cv2.rectangle(ibg, pt1=(ix,iy),pt2=(x,y),color=(0,255,255), thickness=-1)



    elif event == 4:

        flag = False
        cv2.rectangle(ibg, pt1=(ix,iy),pt2=(x,y),color=(0,255,255), thickness=-1)

    #pass

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)

ibg = np.zeros((512,512,3))

while True:
    cv2.imshow("window",ibg)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()