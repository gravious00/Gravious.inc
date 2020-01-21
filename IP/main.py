import numpy as np
import cv2
import pytesseract

img = cv2.imread("1.png")
cv2.imshow("img",img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
smooth = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("smooth", smooth)
edged = cv2.Canny(smooth, 170, 200)
cv2.imshow("edged", edged)
# edged = cv2.Canny(gray, 170, 200)
# cv2.imshow("edged", edged)
#
# smooth = cv2.bilateralFilter(edged, 11, 17, 17)
# cv2.imshow("smooth", smooth)

img1 = img.copy()
img2 = img.copy()
contours, heirarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img1, contours, -1, (255,0,0), 3)
cv2.imshow("New",img1)

contours = sorted(contours, key = cv2.contourArea, reverse=True)[:30]
NumberPlate = None

cv2.drawContours(img2, contours, -1, (255,0,0), 3)
cv2.imshow("New1",img2)

for c in contours:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c, 0.02*peri, True)
    if len(approx) == 4:
        NumberPlate = approx

        x,y,w,h = cv2.boundingRect(c)
        new_img = img[y:y+h,x:x+w]
        cv2.imshow("Crop",new_img)
        text = pytesseract.image_to_string(new_img, lang='eng')
        print("Number is:", text)
        cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
