# This list will store the user movies
movies = []

# Menu implementation
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "


def add_movie():
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


def print_movie(movie):
    print("========================================")
    print(f"title: {movie['title']}")
    print(f"director: {movie['director']}")
    print(f"release year: {movie['release_year']}")


def show_movies():
    print("These are all your movies: \n")
    for movie in movies:
        print_movie(movie)


def find_movie(title):
    movie_found = False

    for movie in movies:
        if movie['title'].lower() == title.lower():
            print_movie(movie)
            movie_found = True
            break
    if not movie_found:
        print("Movie not found.")


selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        add_movie()
        print("The movie was added successfully")
    elif selection == 'l':
        show_movies()
    elif selection == 'f':
        movie_title = input("Type the title of the movie you want to find: ")
        find_movie(movie_title)
    else:
        print("Unknown command. Please try again.")

    selection = input(MENU_PROMPT)
