from imageai.Detection import VideoObjectDetection
from Analysis import convertor as c
import os


def start_analys_frames():
	path = 'Data/'
	file = ['yolo.h5', 'video.avi', 'frames']

	detector = VideoObjectDetection()
	detector.setModelTypeAsYOLOv3()
	detector.setModelPath(path+file[0])
	detector.loadModel()

	video_path = detector.detectObjectsFromVideo(
		input_file_path=path+file[1],
		output_file_path=path+file[2],
		minimum_percentage_probability=40,
		frames_per_second=30,
		log_progress=True
	)

	c.convert()
	
if __name__ == '__main__':
	os.chdir(os.getcwd()[:len(os.getcwd())-9])
	
	start_analys_frames()