# Add type check / type system below...
# import requests
# from bs4 import BeautifulSoup
# import re
# import pandas as pd
import framework_system


# # Downloading imdb top 250 movie's data
# url = 'https://www.imdb.com/event/ev0000292/2013/1'
# #url = 'http://www.imdb.com/chart/top'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# award_data = soup.find_all("script")[39]

# # movies = soup.select('td.titleColumn')
# #awardName = soup.select('td.')
# # crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
# # ratings = [b.attrs.get('data-value')
# #         for b in soup.select('td.posterColumn span[name=ir]')]

# # create a empty list for storing
# # movie information
# list = []
 
# # Iterating over movies to extract
# # each movie's details
# # for index in range(0, len(movies)):
     
# #     # Separating movie into: 'place',
# #     # 'title', 'year'
# #     movie_string = movies[index].get_text()
# #     movie = (' '.join(movie_string.split()).replace('.', ''))
# #     movie_title = movie[len(str(index))+1:-7]
# #     year = re.search('\((.*?)\)', movie_string).group(1)
# #     place = movie[:len(str(index))-(len(movie))]
# #     data = {"place": place,
# #             "movie_title": movie_title,
# #             "rating": ratings[index],
# #             "year": year,
# #             "star_cast": crew[index],
# #             }
# #     list.append(data)

# # for movie in list:
# #     print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
# #           ') -', 'Starring:', movie['star_cast'], movie['rating'])

# print(award_data[3])


def isMovie(movie):
    if framework_system.movies.count(movie) > 0:
        return True
    return False

def isPerson(person):
    if framework_system.people.count(person) > 0:
        return True
    return False

def isShow(show):
    if framework_system.shows.count(show) > 0:
        return True
    return False

def getAwardType(award):
    return framework_system.awards[award]["Nominee Type"]

def isNominee(entity,award):
    if isAwardType(entity,award) == True:
        if framework_system.awards[award]["Nominees"].count(entity) == 1:
            return True
    return False

def isAwardType(entity,award):
    if getAwardType(award) == "Movie":
        if isMovie(entity) == True:
            return True
        return False
    
    elif getAwardType(award) == "Person":
        if isPerson(entity) == True:
            return True
        return False

    elif getAwardType(award) == "Show":
        if isShow(entity) == True:
            return True
        return False


    


