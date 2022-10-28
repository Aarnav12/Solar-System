import cv2

img = cv2.imread("C:/Users/sapsl/Downloads/Whitehat jr Python/C104/Image/solar-system.jpg")


cv2.putText(img,  
           "Sun",
           (85, 100),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "Mercury",
           (125, 190),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "Venus",
           (195, 175),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "Earth",
           (285, 170),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "Mars",
           (380, 180),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "Jupiter",
           (475, 100),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "Saturn",
           (670, 120),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )


cv2.putText(img,  
           "Uranus",
           (965, 140),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "Neptune",
           (1110, 145),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.imshow("output",img)

###### ADDITIONAL ACTIVITY ####

# cv2.imwrite("Greetings.jpg",img)

###############################

cv2.waitKey(0)