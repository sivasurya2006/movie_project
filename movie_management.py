import json

FILE_NAME = "movie.json"


def load_movies():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_movies(movies):
    with open(FILE_NAME, "w") as file:
        json.dump(movies, file, indent=4)


def show_menu():
    print(" MOVIE MANAGEMENT SYSTEM ")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Update Rating")
    print("5. Delete Movie")
    print("6. Sort Movies by Rating")
    print("7. Sort Movies by Release Year")
    print("8. Total Movies")
    print("9. View Movies by Genre")
    print("10. Exit")


def add_movie(movies):
    title = input("Enter movie name: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            print("Movie already exists!")
            return

    genre = input("Enter genre: ").strip()

    try:
        year = int(input("Enter release year: "))
        rating = float(input("Enter rating: "))
    except ValueError:
        print("Invalid input! Year must be a number and rating must be a decimal number.")
        return

    new_movie = {
        "title": title,
        "genre": genre,
        "year": year,
        "rating": rating
    }

    movies.append(new_movie)
    save_movies(movies)
    print("Movie added successfully!")


def view_movies(movies):
    if len(movies) == 0:
        print("No movies found!")
        return

    print("\nMovie List:")
    for movie in movies:
        
        print("Title :", movie["title"])
        print("Genre :", movie["genre"])
        print("Year  :", movie["year"])
        print("Rating:", movie["rating"])


def search_movie(movies):
    title = input("Enter movie name to search: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            print("Movie found!")
            print(movie)
            return

    print("Movie not found!")


def update_rating(movies):
    title = input("Enter movie name to update rating: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            try:
                new_rating = float(input("Enter new rating: "))
            except ValueError:
                print("Invalid rating! Please enter a number.")
                return

            movie["rating"] = new_rating
            save_movies(movies)
            print("Rating updated successfully!")
            return

    print("Movie not found!")


def delete_movie(movies):
    title = input("Enter movie name to delete: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            movies.remove(movie)
            save_movies(movies)
            print("Movie deleted successfully!")
            return

    print("Movie not found!")


def sort_movies_by_rating(movies):
    if len(movies) == 0:
        print("No movies found!")
        return

    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    print("\nMovies Sorted by Rating:")
    for movie in sorted_movies:
        print(movie["title"], "-", movie["rating"])


def sort_movies_by_year(movies):
    if len(movies) == 0:
        print("No movies found!")
        return

    sorted_movies = sorted(movies, key=lambda movie: movie["year"])

    print("\nMovies Sorted by Release Year:")
    for movie in sorted_movies:
        print(movie["title"], "-", movie["year"])


def total_movies(movies):
    print("Total number of movies:", len(movies))


def view_movies_by_genre(movies):
    genre = input("Enter genre: ").strip()
    found = False

    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            print(movie)
            found = True

    if not found:
        print("No movies found in this genre!")


movies = load_movies()

while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number.")
        continue

    if choice == 1:
        add_movie(movies)
    elif choice == 2:
        view_movies(movies)
    elif choice == 3:
        search_movie(movies)
    elif choice == 4:
        update_rating(movies)
    elif choice == 5:
        delete_movie(movies)
    elif choice == 6:
        sort_movies_by_rating(movies)
    elif choice == 7:
        sort_movies_by_year(movies)
    elif choice == 8:
        total_movies(movies)
    elif choice == 9:
        view_movies_by_genre(movies)
    elif choice == 10:
        print("Thank you for using Movie Management System!")
        break
    else:
        print("Invalid choice! Please select 1 to 10.")