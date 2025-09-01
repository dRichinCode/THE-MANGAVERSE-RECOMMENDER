import pytest
from project import include_genre_identifier, exclude_genre_identifier, apply_filters

def test_include_genre_identifier():
    genres_sets = {"Action", "Adventure", "Comedy"}

    included_genres = {"Action", "Adventure"}
    assert include_genre_identifier(genres_sets, included_genres) == True

    included_genres = {"Comedy", "Action"}
    assert include_genre_identifier(genres_sets, included_genres) == True

    included_genres = {"Action", "Horror"}
    assert include_genre_identifier(genres_sets, included_genres) == False

    included_genres = {"Fantasy", "Adventure"}
    assert include_genre_identifier(genres_sets, included_genres) == False



def test_exclude_genre_identifier():
    excluded_genres = {"Thriller", "Horror", "Drama"}

    genres_sets = {"Action", "Adventure", "Comedy"}
    assert exclude_genre_identifier(genres_sets, excluded_genres) == True

    genres_sets = {"Comedy", "Action", "Fantasy", "Romance"}
    assert exclude_genre_identifier(genres_sets, excluded_genres) == True

    genres_sets = {"Thriller", "Action"}
    assert exclude_genre_identifier(genres_sets, excluded_genres) == False

    genres_sets = {"Drama", "Adventure", "Comedy"}
    assert exclude_genre_identifier(genres_sets, excluded_genres) == False




def test_apply_filters():
    csv_data = [
        {"Title": "Naruto", "Genres": "Action, Ninja, Comedy, Martial Arts, Adventure, Drama", "Status": "Completed", "Year": 1999,
          "Description": "Naruto works toward his dream of becoming the Hokage, the best ninja in the village with his fellow friends Sasuke and Sakura and mentor Kakashi as they go through many trials and battles that come with being a ninja."},
        {"Title": "20th Century Boys", "Genres": "Sci-Fi, Drama, Psychological", "Status": "Completed", "Year": 1999,
         "Description": "This is the story of a group of friends and classmates try to solve world-ending issues and mysteries all around the globe, believing that they might be the cause, the question they keep asking is will they be able to save the world"},
        {"Title": "Blue Box", "Genres": "Romance, Comedy, School Life, Sports", "Status": "Ongoing", "Year": 2021,
         "Description": "Taiki Inomata is on the boys' badminton team at sports powerhouse Eimei Junior and Senior High. He's in love with the older girl basketball player Chinatsu Kano. One Spring day, their relationship takes a sharp turn ... And thus begins this brand-new series of love, sports and youth!"} ]

    included_genres = {"Action", "Adventure", "Martial Arts"}
    excluded_genres = {"Sci-Fi", "School Life"}
    status = "Completed"
    start = 1999
    end = 2022

    result = apply_filters(csv_data, included_genres, excluded_genres, status, start, end)
    assert len(result) == 1
    assert result[0]["title"] == "Naruto"
    assert apply_filters(csv_data, {"Aliens"}, {"Psychological"}, "Ongoing", 2011, 2019) == []

