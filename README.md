# THE MANGAVERSE RECOMMENDER
#### Video Demo: <https://www.youtube.com/watch?v=eTFz347AbcU>
#### Description:

The MangaVerse Recommender solves the problem that all dedicated manga fans face around the globe: finding the right manga. With thousands of titles, it is a brutal chore to find a manga that specifically appeals to you. Perhaps you did not realize it was an ongoing series when you would have preferred a completed story. Possibly, you wanted to read a fantasy manga set in a school setting with a hint of romance, but you don’t want action or fighting in it. The MangaVerse Recommender filters out those conditions for you.

The MangaVerse Recommender asks the user for their conditions/preferences for what type of manga they want to read, which narrows the program's search. It mainly requests them to answer four questions: which genre they would prefer to read, which genre they would prefer to avoid, whether they would like a completed or ongoing title, and what decade they would like to read from.


 ### How To Run:
 1. Download or clone the project
 2. Install the most recent Python version
 3. Make sure that mangas_list.csv is in the same folder as the program
 4. Run it by calling it from the terminal


### The Key Functions of The MangaVerse Recommender:
- **main()** - The function that connects every function together.
- **read_csv()** - This function allows multiple functions to use the data from the manga_list (CSV file) and makes parsing the data easier.
- **display_genres()** - Displays all the available genres the user can choose from. This function is integral as it collects the genres the user selects, which helps narrow down the titles.
- **leftover_genres()** - Presents all the available genres the user prefers to avoid. This function is important as it collects the genres the user selects, which helps narrow down the titles they don't want to see.
- **status_recommender()** - Displays only two options to the user, asking whether they want their manga to be completed or ongoing.
- **year_recommender()** - With six decades (from the 1970s to the 2020s), this function inquires about the decade the user would like to read from.
- **apply_filters()** - Arguably the most significant function in the program, as it collects and compares the manga_list (CSV file) with all of the conditions the user entered. It goes through every title to check whether it meets their conditions or not.
- **limit_results()** - After apply_filters() identifies every manga that meets the user's conditions, it asks the user how many titles they would like to see, improving the user experience. This function creates two variables: one counting how many titles were found and another representing how many titles the user would preferably see. It then compares these two values and displays the smaller number of titles.


### The Extra Functions of The MangaVerse Recommender:
- **choices_displayer()** - This is a straightforward function. It takes a list and displays it in a clean and horizontal way with spaces. I just added it to make the genres look cleaner.
- **include_genre_identifier()** - This checks whether **all genres** inputted by the user are **present** in the title.
- **exclude_genre_identifier()** - This checks whether **all genres** inputted by the user that they would like to avoid are **not present** at all in a title.


### Design Decisions:
- This program gets its data from a CSV file of a list of mangas from differing genres, statuses, and years. I manually cleaned this file to get the results I wanted. I did it this way as I deduced that it would make the code simpler to make and understand. I was originally going to use an API because they generally update automatically, whereas CSV files require you or someone else to manually edit them. However, every API I found had a learning curve that I am not prepared to face just yet. Also, I found that I preferred making my program work offline.


### Challenges & Solutions:
- During the very early stages of development, I realized that the info from the CSV file got mixed up. The titles weren't getting their designated genres, statuses, descriptions, and years. I first checked and cleaned up my CSV file just to make sure, and I reworked my read_csv() function, and it solved my issue.


### Future Improvements & Potential:
- I see a lot of ways this program could be better. Have more titles in the Manga List CSV file, make more filters—perhaps by user ratings, length, and more. I could see that being achieved through adding more columns, filtering by the user's minimum amount of ratings required, or the maximum amount of chapters they deem acceptable. I could also see this program being used for other types of media. I would prefer more niche ones like manhwas or manhua, but this program being used for regular books would be great too.


### Conclusion:
- This project was challenging but fun to conceptualize and program. I have used this for myself, and I have gotten some titles that caught my eye. I hope the users of this project will find an engaging manga to read. I don't regret choosing The MangaVerse Recommender as my final project for this course. I believe it met the perfect balance of complex and simple for me. When I understood one part, I understood how to develop the other parts even more. I also learned different tools from Python, like subsets and disjoints, or how in dictionaries you can use sets for values to do ranges. It was all gratifying to learn and grow in. I believe this project solidified how I solve problems—just by cutting it into smaller parts, all would be manageable. Through this project, I was able to give a user experience the exact way I wanted to portray it. I look forward to this feeling and similar experiences in my future projects.
