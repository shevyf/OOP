import webbrowser

class Media():
    def __init__(self,
                 title,
                 description,
                 poster_image_url,
                 running_time,
                 genre):
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.running_time = running_time
        self.genre = genre

class Movie(Media):
    def __init__(self,
                 title,
                 description,
                 poster_image_url,
                 running_time,
                 genre,
                 youtube_trailer,
                 rating):
        Media.__init__(self, title, description, poster_image_url, running_time, genre)
        self.trailer_youtube_url = youtube_trailer
        self.rating = rating

    def play_trailer(self):
        webbrowser.open(self.youtube_trailer)

class TVShow(Media):
    def __init__(self,
                 title,
                 description,
                 poster_image_url,
                 running_time,
                 genre,
                 imdb_episode_list,
                 episode_count):
        Media.__init__(self, title, description, poster_image_url, running_time, genre)
        self.imdb_episode_list = imdb_episode_list
        self.episode_count = episode_count

    def display_info(self):
        pass
