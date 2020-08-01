def main():
	#Hello!
	if input('Use gui interafce? (+): '):
		from Gui import interface
		interface.MainApp().run()

	else:
		if input('\nOpen camera? (+): '):
			from Record import recorder 
			recorder.start_record()

		if input('\nAnalys speech? (+): '):
			from Analysis import speech
			speech.start_analys_speech()

		if input('\nAnalys photo? (+): '):
			from Analysis import photo 
			photo.start_analys_frame()

		if input('\nAnalys video? (+): '):
			from Analysis import video 
			video.start_analys_frames()
		
		if input('\nShow video? (+): '):
			from Record import player
			player.start_play()

		if input('\nShow speech? (+): '):
			from Record import player
			text = player.show_speech()	
			print(text)

		if input('\nShow photo? (+): '):
			from Record import player
			player.show_photo()


if __name__ == '__main__':
	main()