import cv2
import time
import pyaudio
import wave
import sys
import os
import time
from threading import Thread


status = False


def video():
	global status

	cap = cv2.VideoCapture('Data/video.avi')

	# time.sleep(0.21)
	try:
		while(cap.isOpened()):
			if status or cv2.waitKey(1) == ord('q'):
				status = True
				break

			ret, frame = cap.read()
			cv2.imshow('Videoplayer',frame)
	except:
		pass

	cap.release()
	cv2.destroyAllWindows()


def audio():
	global status
	chunk = 1024
	wf = wave.open('Data/audio.wav', 'rb')
	p = pyaudio.PyAudio()
	data = wf.readframes(chunk)

	stream = p.open(
		format=p.get_format_from_width(wf.getsampwidth()),
	    channels=wf.getnchannels(),
	    rate=wf.getframerate(),
	    output=True)

	for i in data:
		stream.write(data)
		data = wf.readframes(chunk)

		if status or cv2.waitKey(1) == ord('q'):
			status = True
			break
	 
	stream.stop_stream()
	stream.close()
	p.terminate()


def start_play():
	thread1 = Thread(target=video)
	thread2 = Thread(target=audio)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

def show_photo():
	frame = cv2.imread('Data/frame.jpg')

	while True:
		if cv2.waitKey(1) == ord('q'):
			break
			
		cv2.imshow('Picture', frame)

	cv2.destroyAllWindows()

def show_speech():

	with open('Data/speech.txt') as f:
		return f.read()


if __name__ == '__main__':

	os.chdir(os.getcwd()[:len(os.getcwd())-7])

	if input('\nShow video? (+): '):
		start_play()

	if input('\nShow speech? (+): '):
		text = show_speech()	
		print(text)

	if input('\nShow photo? (+): '):
		show_photo()