import csv
import random
GENRES = [
    "4-Koma", "Action", "Adaptation", "Adventure", "Aliens", "Animals", "Anthology", "Award Winning",
    "Boys' Love", "Comedy", "Cooking", "Crime", "Crossdressing", "Delinquents", "Demons", "Doujinshi",
    "Drama", "Fantasy", "Full Color", "Genderswap", "Ghosts", "Girls' Love", "Gore", "Gyaru",
    "Harem", "Historical", "Horror", "Isekai", "Mafia", "Magic", "Magical Girls", "Martial Arts",
    "Mecha", "Medical", "Military", "Monster Girls", "Monsters", "Music", "Mystery", "Ninja",
    "Office Workers", "Official Colored", "Oneshot", "Philosophical", "Police", "Post-Apocalyptic",
    "Psychological", "Reincarnation", "Reverse Harem", "Romance", "Samurai", "School Life",
    "Sci-Fi", "Self-Published", "Slice of Life", "Sports", "Superhero", "Supernatural",
    "Survival", "Thriller", "Time Travel", "Traditional Games", "Tragedy", "Vampires",
    "Video Games", "Villainess", "Virtual Reality", "Web Comic", "Wuxia", "Zombies"
]

year_ranges_dict = {
    "1970s": (1970, 1980), "1980s": (1981, 1990), "1990s": (1991, 2000),
    "2000s": (2001, 2010), "2010s": (2011, 2020), "2020s": (2021, 2025)
}


def main():
    manga_list = "mangas_list.csv"
    csv_data = read_csv(manga_list)
    input(f"HELLO, and WELCOME to THE MANGAVERSE RECOMMENDER\npress enter to move on")  
    included_genres = set(display_genres())
    excluded_genres = set(leftover_genres(set(included_genres)))
    status = status_recommender()
    included_years = year_recommender()
    start, end = included_years
    filtered_titles = apply_filters(csv_data, included_genres,
                                    excluded_genres, status, start, end)
    limit_results(filtered_titles)










# This reads the csv_file(manga_list) and returns the data through lists and dictionaries
def read_csv(manga_list):
    data = []
    with open(manga_list, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


# This shows the entire list(GENRES) and it gets an input of what genre the user wants to see
# if they press 's' they would get 5 random genres
# The input should be formatted "genre_1, genre_2, genre_3" if not they would reprompt
def display_genres():
    print("\nAVAILABLE GENRES:\n")
    choices_displayer(GENRES)
    while True:
        raw_input = input(
            "\nType the Genres you want to include (At least two, ex. Action, Adventure)\n(press s to get random genres): ").strip().title()
        if raw_input.lower() == "s":
            included_genres = random.sample(GENRES, k=5)
            break
        else:
            included_genres = raw_input.split(", ")
            if all(genre in GENRES for genre in included_genres):
                break
            else:
                print("Invalid input for included genres :( Please try again.")

    return included_genres


# Makes a new list(remaining_genres) which is made by deducting GENRES and included_genres
# This shows the remaining_genres and it gets an input of what genre the user doesn't want to see
# If they press 's' they would get 3 random genres
# The input should be formatted "genre_1, genre_2, genre_3" if not they would reprompt
def leftover_genres(included_genres):
    remaining_genres = set(GENRES) - set(included_genres)
    remaining_genres = sorted(list(remaining_genres))
    print("\nLEFTOVER GENRES:\n")
    choices_displayer(remaining_genres)

    while True:
        raw_input = input(
            "\n\nType the Genres you want to exclude (At least two, ex. Action, Adventure)\n(press s to get random genres): ").strip().title()
        if raw_input.lower() == "s":
            excluded_genres = random.sample(remaining_genres, k=3)
            break
        else:
            excluded_genres = raw_input.split(", ")
            if all(genre.strip() in remaining_genres for genre in excluded_genres):
                break
            else:
                print("Invalid input for excluded genres :( Please try again.")

    return excluded_genres


# This function displays the choices in a clean way
# Instead of the vertical way it would be horizontal
def choices_displayer(choices):
    width = len(str(len(choices))) + 2
    for index, choice in enumerate(choices, start=1):
        print(f"{index:>{width}}. {choice:<20}", end="   ")
        if (index % 5 == 0):
            print()
    print()


# This give the user the choice whether they want the title/s to be Completed or Ongoing
# They also have the choice to get a random status by pressing 's'
# It also validates the input, it reprompts if its not a valid answer
def status_recommender():
    statuses = ["Completed", "Ongoing"]
    print(f"\n1. {statuses[0]}\n2. {statuses[1]}")
    while True:
        status = input(
            f"\nChoose between {statuses[0]} or {statuses[1]}\n(press 's' to get a random status): ").strip().title()
        if status == "S":
            status = random.choice(statuses)
            break
        elif status in statuses:
            break
        else:
            print("Invalid input for status :( Please try again.")

    return status


# This shows the keys(year_ranges_keys) of dictionary(year_ranges_dict)
# The values are the sets of that specific range
# They also have the choice to get a random year by pressing 's'
# The year_ranges_keys are weighted, the highest is 2010s and the further it is from 2010s the lower the chance of it being picked
# It also validates the input, it reprompts if its not a valid answer
def year_recommender():
    print("\nPICK A YEAR RANGE:")
    year_ranges_keys = list(year_ranges_dict.keys())
    for i, key in enumerate(year_ranges_keys, start=1):
        print(f"{i}. {key:<10}", end=" ")
    print()

    while True:
        pref_year_range = input("YEAR RANGE (press 's' to get a random year range): ").strip()
        if pref_year_range.lower() == "s":
            pref_year_range = random.choices(year_ranges_keys, weights=[
                                             5, 10, 15, 25, 50, 25], k=1)[0]
            break
        elif pref_year_range in year_ranges_keys:
            break
        else:
            print("Invalid input for year range :( Please try again.")

    included_years = year_ranges_dict.get(pref_year_range)
    return included_years


# This is the most integral part of the entire program
# It creates a list(filtered_titles) which would contain dictionaries, 1 title per dictionary each
# Each element/dictionary of the list contains the title and description of that specific manga
# It reads the entire data of the csv_data
# After reading, it finds every info of that specific manga (Genres,Status,Year,Title,Description) and assign a new variable
# This function takes every argument(inputs from the user) so far
# This function finds the manga that matches all the conditions that the user inputted
def apply_filters(csv_data, included_genres, excluded_genres, status, start, end):
    filtered_titles = []
    for row in csv_data:
        titles = row["Title"]
        statuses = row["Status"]
        genres_sets = set(row["Genres"].split(", "))
        years = int(row["Year"])
        description = row["Description"]
        if (include_genre_identifier(genres_sets, included_genres) and statuses == status) and (exclude_genre_identifier(genres_sets, excluded_genres) and start <= years <= end):
            filtered_titles.append({"title": titles, "description": description})
    return filtered_titles

# This function takes the genres from the csv_data and the genres the user specifically wants to see
# Checks which set of genres_sets where every genre of included_genres is present


def include_genre_identifier(genres_sets, included_genres):
    return included_genres.issubset(genres_sets)

# This function takes the genres from the csv_data and the genres the user specifically doesn't want to see
# Checks which set of genres_sets that aren't present in the excluded_genres


def exclude_genre_identifier(genres_sets, excluded_genres):
    return excluded_genres.isdisjoint(genres_sets)


# Gives the user the choice how many titles they want to see at most
# The answer is validated by checking whether they inpputed more than 0, reprompts if it doesn't
# Calculates how many titles did the filtered_titles found
# Finds what is smaller between pref_maximum & act_maximum, to determine how many titles it would show
# If pref_maximum > act_maximum it would print noting that the program only found a smaller amount of mangas based on the user's conditions
# It shows what title and description of the manga found
def limit_results(filtered_titles):
    if filtered_titles:
        while True:
            try:
                pref_maximum = int(input("How many titles do you wanna see (at most, ex. 3): "))
                act_maximum = len(filtered_titles)
                if pref_maximum > 0:
                    limited_titles = random.sample(
                        filtered_titles, k=min(pref_maximum, act_maximum))
                    if pref_maximum > act_maximum:
                        print(f"Only {act_maximum} titles available. Showing all of them \nHope you find something interesting :)")
                    for title in limited_titles:
                        print(f"Title: {title['title']}")
                        print(f"Synopsis: {title['description']}\n")
                    break
                elif pref_maximum <= 0:
                    continue
            except ValueError:
                print("Please enter a number that is more than 0.")
                continue
    else:
        print("NOTHING FOUND :(\nLet's Try Again :)")


if __name__ == "__main__":
    main()
