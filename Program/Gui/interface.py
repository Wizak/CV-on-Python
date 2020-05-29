import os

from kivy.app import App
from kivy.config import Config

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


WIDTH, HEIGHT = 400, 600

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', WIDTH)
Config.set('graphics', 'height', HEIGHT)


class MainApp(App):

	def open_camera(self, instance):

		from Record import recorder 
		recorder.start_record()

	def analys_speech(self, instance):

		from Analysis import speech
		speech.start_analys_speech()

	def analys_photo(self, instance):

		from Analysis import photo
		photo.start_analys_frame()

	def analys_video(self, instance):

		from Analysis import video
		video.start_analys_frames()

	def shower_speech(self, instance):

		from Record import player

		f_size = '15px'
		h_size = [.9, .9]
		text = player.show_speech()

		self.lbl = Label(
			text=' '*5+text, 
			font_size=f_size, 
			size_hint=h_size,
            )

		self.layout1.add_widget(self.lbl)

	def shower_photo(self, instance):

		from Record import player
		player.show_photo()

	def shower_video(self, instance):

		from Record import player
		player.start_play()

	def build(self):

		f_size = '25px'
		h_size = [.5, .5]
		n = 16
		self.text = ''

		self.layout1 = BoxLayout(orientation='vertical')
		layout2 = BoxLayout(orientation='horizontal')
		layout3 = BoxLayout(orientation='horizontal')

		self.layout1.add_widget(Label(
			text='  '*n+'Open', 
			font_size=f_size, 
			size_hint=h_size,
            ))

		self.layout1.add_widget(Button(
			text='Camera', 
			font_size=f_size, 
			background_color=[1, 1, 1, 1], 
			background_normal='',
			color=[0, 0, 0, 1],
			on_press=self.open_camera
			))

		lay = [layout2, layout3]
		but = ['Speech', 'Photo', 'Video']
		cat = ['Analysis', 'Show']

		method = {
			cat[0]: {
				but[0]: self.analys_speech, 
				but[1]: self.analys_photo, 
				but[2]: self.analys_video
				}, 

			cat[1]: {
				but[0]: self.shower_speech, 
				but[1]: self.shower_photo, 
				but[2]: self.shower_video
				} 
			}

		for i, j in zip(lay, cat):

			self.layout1.add_widget(Label(
				text='  '*n+j, 
				font_size=f_size, 
				size_hint=h_size,
				))

			self.layout1.add_widget(i)

			for k in but:

				i.add_widget(Button(
					text=k, 
					font_size=f_size, 
					background_color=[1, 1, 1, 1], 
					background_normal='',
					color=[0, 0, 0, 1],
					on_press=method[j][k]
					))

		return self.layout1


if __name__ == '__main__':
	os.chdir(os.getcwd()[:len(os.getcwd())-4])
	MainApp().run()