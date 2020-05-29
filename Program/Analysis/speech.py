import os
import speech_recognition as sr 


def start_analys_speech():
	audio = ("Data/audio.wav")
	r = sr.Recognizer()

	with sr.AudioFile(audio) as source:
		audio = r.record(source)  

	try: 
		file = open('Data/speech.txt', 'w')
		file.write(r.recognize_google(audio))
		file.close()

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio.")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service: {0}".format(e))


if __name__ == '__main__':
	os.chdir(os.getcwd()[:len(os.getcwd())-9])

	start_analys_speech()