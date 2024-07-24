#importing the opencv module  
import cv2

# using imread('path') and 0 denotes read as  grayscale image and 1 denotes read as RGB
img = cv2.imread(r"src/tata_logo.png",1)

#This is using for display the image 
cv2.imshow('Tata_logo',img)

#This is using for save the image  
cv2.imwrite("src/TATA.png",img)


# This is necessary to be required so that the image doesn't close immediately. 
# 0 means wait indefinitely or for a specific amount of time (e.g., 5000 ms)
cv2.waitKey(5000)

#It will run continuously until the key press. 
cv2.destroyAllWindows()