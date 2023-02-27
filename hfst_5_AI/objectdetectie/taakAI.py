from PIL import Image
import pytesseract
import numpy as np
import cv2
import pathlib
import os
import keyboard
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  
# define a video capture object
vid = cv2.VideoCapture(1)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if vid:
        # show the image
        cv2.imshow('frame', frame)
        
        # save the image
        if keyboard.is_pressed('s'):
            path = str(pathlib.Path(__file__).parent.resolve())
            cv2.imwrite(os.path.join(path,"foto.png"), frame)
            filename = os.path.join(path,"foto.png")
            img = np.array(filename)
            norm_img = np.zeros((img.shape[0], img.shape[1]))
            img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
            img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
            text = pytesseract.image_to_string(img)
            print(text)
            print("oke")
    else:
        print("error")
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()