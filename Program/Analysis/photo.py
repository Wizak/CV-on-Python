from imageai.Detection import ObjectDetection
import os


def start_analys_frame():
	path = 'Data/'
	file = ['resnet50_coco_best_v2.0.1.h5', 'photo.jpg', 'frame.jpg']

	try:
		detector = ObjectDetection()
		detector.setModelTypeAsRetinaNet()
		detector.setModelPath(path+file[0])

		detector.loadModel()

		list = detector.detectObjectsFromImage(
			input_image=path+file[1],
			output_image_path=path+file[2],
			minimum_percentage_probability=40,
			display_percentage_probability=True,
			display_object_name=True
		)
	except:
		pass


if __name__ == '__main__':
	os.chdir(os.getcwd()[:len(os.getcwd())-9])

	start_analys_frame()