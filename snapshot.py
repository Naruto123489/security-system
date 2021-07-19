import cv2


#defining the function
def take_snapshot():
    #start the webcam
    videoCaptureObject = cv2.VideoCapture(0)    
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        print(ret)
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result = False

    #close the webcam
    videoCaptureObject.release()
    # to close any opened windows by the camera
    cv2.destroyAllWindows()

#calling the function
take_snapshot()
