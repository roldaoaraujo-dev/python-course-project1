# This list will store the user movies
movies = []

# Menu implementation
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "


def movie_add():
    # Getting input from the user
    title = input("Type the movie title: ")
    director = input("Type the movie director: ")
    release_year = input("Type the movie release year: ")

    movie = {
        "title": title,
        "director": director,
        "release_year": release_year
    }
    movies.append(movie)


selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        movie_add()
        print("The movie was added successfully")
    elif selection == 'l':
        pass
    elif selection == 'f':
        pass
    else:
        print("Unknown command. Please try again.")

    selection = input(MENU_PROMPT)
