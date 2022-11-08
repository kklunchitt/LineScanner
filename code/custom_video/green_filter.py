import cv2
import numpy as np
# Create a VideoCapture object and read from input file
# If the unput is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('/Users/kawinklunchitt/Desktop/Senior Year/EE Project/Code/LineScanner/images/laser1a_720.mp4')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('/Users/kawinklunchitt/Desktop/Senior Year/EE Project/Code/LineScanner/code/custom_video/output.mp4', fourcc,  20.0, (640,480))
# Check if camera opened successfully
if (cap.isOpened()==False):
    print("Error oening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    # Capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Threshold of Green 
        lower_green = np.array([40,60,255])
        upper_green = np.array([60,80,255])

        # Preparing the mask to overlay
        mask = cv2.inRange(hsv, lower_green,upper_green)

        # The black region in the mask has the value of 0.
        # so when nultiplied with original image removes all non-green
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Display the resulting frame
        cv2.imshow("frame", frame)
        cv2.imshow('Result', result)
        cv2.imshow('Mask',mask)
        out.write(result)
        # Press Q on keyboard to exit
        if cv2.waitKey(1) == ord('q'):
            break
    
    # Break the loop
    else:
        break
# When everything done, release the video capture object
out.release()
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
