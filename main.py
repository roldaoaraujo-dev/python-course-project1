# This list will store the user movies
movies = []

# This will be the structure of each movie
movie = {
    "title": "",
    "director": "",
    "release_year": 0
}
# Menu implementation
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == 'a':
        pass
    elif selection == 'l':
        pass
    elif selection == 'f':
        pass
    else:
        print("Unknown command. Please try again.")

    selection = input(MENU_PROMPT)
