import cv2

img = cv2.imread("C:/Users/sapsl/Downloads/Whitehat jr Python/C104/Image/solar-system.jpg")

text_to_show = "Sun"


cv2.putText(img,  
           text_to_show,
           (85, 100),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.imshow("output",img)

###### ADDITIONAL ACTIVITY ####

# cv2.imwrite("Greetings.jpg",img)

###############################

cv2.waitKey(0)