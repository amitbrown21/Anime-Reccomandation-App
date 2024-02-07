from time import sleep

from icecream import ic

from jikanpy import Jikan

jikan = Jikan()
anime_type = 'tv'
min_score = 7
anime_r = []
genre = 'Comedy'
anime_list = []
seasons = ['spring', 'summer', 'winter', 'fall']
for year in range(2010, 2011 + 1):
    for s in seasons:
        anime_season = jikan.seasons(year=year, season=s,
                                     parameters={'filter': anime_type})['data']
        anime_list.append(anime_season)
        sleep(0.7)
for anime in anime_list:
    for an in anime:
        an_genre = an['genres']
        ic = an_genre
        an_score = an['score']
        if an_score is not None and any(ge['name'] == genre for ge in an_genre) and an_score >= min_score:
            anime_r.append(an)

print(anime_r)
