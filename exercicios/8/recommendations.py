import os
import json


with open("filmes.json", mode="r", encoding="utf8") as fd:	
	age = int(input("Qual sua idade? "))
	favorite_category = str(input("Qual seu gênero favorito? "))

	movies = dict(json.loads(fd.read())).get('movies')
	
	def filter_by_genre(movie):
		if favorite_category in movie.get('genres'):
			return True
		return False
	
	def filter_by_age(movie):
		print(movie)
		if age >= movie.get('recommended_age'):
			return True
		return False
		
	# first by genre
	filtered_movies = list(filter(filter_by_genre, movies))
	filtered_age = list(filter(filter_by_age, filtered_movies))

	print(filtered_age[0:3])