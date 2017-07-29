import webbrowser

class Media():
	"""docstring for Media"""
	def __init__(self, title):
		self.title = title


class Movie(Media):
	"""docstring for Movie"""
	def __init__(self, title, storyline, poster,url):
		Media.__init__(self,title)
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = url

	def show_movie(self):
		webbrowser.open(self.url)
		
		