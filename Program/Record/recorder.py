import numpy as np
from threading import Thread
import os
import cv2
import pyaudio
import wave
import time


status_camera, status = False, True


class VideoRecorder():

    def __init__(self):
        self.filename = 'Data/video.avi'
        self.path = 'Data/photo.jpg'
        self.fps = 110
        self.res = (1280, 720)
        self.forucc = cv2.VideoWriter_fourcc(*'XVID')
        self.cap = cv2.VideoCapture(0)
        self.out = cv2.VideoWriter(self.filename, self.forucc, self.fps, self.res)
        self.cap.set(3, self.res[0])
        self.cap.set(4, self.res[1])
        self.ret, self.frame = 0, 0

    def show(self):
        global status, status_camera

        while True:
            self.ret, self.frame = self.cap.read()
            cv2.imshow('Camera', self.frame)

            if status_camera or cv2.waitKey(1) == ord('q'):
                status_camera, status = True, True
                break  

        cv2.imwrite(self.path, self.frame)
        self.cap.release()
        cv2.destroyAllWindows()

    def record(self):
        global status

        while True:
            self.out.write(self.frame)

            if status or cv2.waitKey(1) == ord('q'):
                status = True
                break  

        self.out.release()       

class AudioRecorder():

    def __init__(self):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate= 44100
        self.limit = 5
        self.output = "Data/audio.wav"
        self.stream = 0

    def record(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.format,
                    channels=self.channels,
                    rate=self.rate,
                    input=True,
                    frames_per_buffer=self.chunk)

        self.process()

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        self.file()

    def process(self):
        global status
        self.frames = []

        while True:
            if status or cv2.waitKey(1) == ord('q'):
                status = True
                break

            self.data = self.stream.read(self.chunk)

            self.frames.append(self.data)

    def file(self):
        self.wf = wave.open(self.output, 'wb')
        self.wf.setnchannels(self.channels)
        self.wf.setsampwidth(self.p.get_sample_size(self.format))
        self.wf.setframerate(self.rate)
        self.wf.writeframes(b''.join(self.frames))
        self.wf.close()


def player(video, audio):
    global status, status_camera

    thread1 = Thread(target=video.record)
    thread2 = Thread(target=audio.record)
    
    if input('\nRecord ON -> (+): ') == '+':
        status = False

        thread1.start()
        thread2.start()

    if input('Record OFF -> (+): ') == '+':
            status = True

            thread1.join()
            thread2.join()

    if input('\nExit camera -> (+): ') == '+':
            status = True
            status_camera = True

def start_record():    
    video = VideoRecorder()
    audio = AudioRecorder()

    thread1 = Thread(target=video.show)
    thread2 = Thread(target=player, args=(video, audio))

    thread1.start()
    thread2.start()  

    thread1.join()
    thread2.join()

if __name__ == '__main__':
    os.chdir(os.getcwd()[:len(os.getcwd())-7])

    start_record()