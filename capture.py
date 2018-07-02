import cv2
import time
import numpy as np

def nothing(x):
    pass
image_x, image_y = 200,200

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0


cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

while True:
    total_pic = 5
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)

    

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    imcrop = img[102:298, 427:623]
    hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
 
    result = cv2.bitwise_and(imcrop, imcrop, mask=mask)
    
    cv2.putText(frame, str(img_counter), (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (127, 127, 255))
    cv2.imshow("test", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    
    if cv2.waitKey(1) == ord('c'):
        img_name = "{}.png".format(img_counter)
        #imcrop = mask[102:298, 427:623]
        #gray = cv2.cvtColor(imcrop, cv2.COLOR_BGR2GRAY)
        save_img = cv2.resize(mask, (image_x, image_y))
        cv2.imwrite(img_name, save_img)
        print("{} written!".format(img_name))
        img_counter += 1
        

    elif cv2.waitKey(1) == 27:
        break

    if img_counter == total_pic:
        break

cam.release()
cv2.destroyAllWindows()