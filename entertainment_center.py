# This file defines instances of the class Movie defined in media.py. 

import media
import fresh_tomatoes

back_to_the_future = media.Movie("Back to the Future", "Storyline",
	"https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg", 
	"https://www.youtube.com/watch?v=qvsgGtivCgs")

star_trek = media.Movie("Star Trek: Into Darkness", "Captain Kirk and Spock face Khan.", 
	"https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",
	"https://www.youtube.com/watch?v=r5gdbUC9mWU")

inception = media.Movie("Inception", "A professional thief commits corporate espionage by infiltrating the subconscious of his targets through their dreams.",
	"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
	"https://www.youtube.com/watch?v=1g4PLj0PlOM")

mission_impossible = media.Movie("Mission Impossible: Ghost Protocol", "Storyline",
	"https://upload.wikimedia.org/wikipedia/en/b/b5/Mission_impossible_ghost_protocol.jpg",
	"https://www.youtube.com/watch?v=novQIyjFwJA")

star_wars = media.Movie("Star Wars Episode III: Revenge of the Sith", "Storyline",
	"https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
	"https://www.youtube.com/watch?v=5UnjrG_N8hU")

the_dark_knight = media.Movie("The Dark Knight", "Storyline",
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [back_to_the_future, star_trek, inception, mission_impossible, star_wars, the_dark_knight]

fresh_tomatoes.open_movies_page(movies)
