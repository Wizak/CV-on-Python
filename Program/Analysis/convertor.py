import cv2
import os
import time
from threading import Thread 


def convert():
    
    filename = 'Data/frames_new.avi'
    fps = 110
    res = (1280, 720)
    forucc = cv2.VideoWriter_fourcc(*'XVID')

    cam = cv2.VideoCapture("Data/frames.avi")
    out = cv2.VideoWriter(filename, forucc, fps, res)

    try:
        while True:
            ret, frame = cam.read()
            frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame1)
    except:
        pass

    out.release() 
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    os.chdir(os.getcwd()[:len(os.getcwd())-9])
    convert()