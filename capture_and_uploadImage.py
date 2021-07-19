import random
import cv2
import time
import dropbox

start_time= time.time()

#function which uses random number to generate random id for images and returns path of the image
def take_snapshot():
    number = random.randint(0,100) 
    #start the webcam
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img" + str(number) + '.png'
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False    
    return img_name
    print("snapshot taken")
    #close the webcam
    videoCaptureObject.release()
    # to close any opened windows by the camera
    cv2.destroyAllWindows()

def upload_image(img_name):
    access_token = 'OvvKNjrGAUYAAAAAAAAAAbuQl_KvKcUyplPCTXvvxk9Ehld6wVf_b6bOXaOe0H9W'
    file = img_name
    file_from = file
    file_to = '/newFolder/' + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")



def main():
    while(True):
        if ((time.time() -  start_time) >= 5):
            name = take_snapshot()
            upload_image(name)

main()
