# Movie Management System

A beginner-friendly Python command-line application for managing movie records using JSON file storage.

## Overview

Movie Management System is a simple CRUD-based Python project that allows users to add, view, search, update, delete, sort, and filter movie records.

The movie data is stored in a `movie.json` file, which means the records are saved even after the program is closed.

## Features

- Add new movie records
- View all saved movies
- Search movies by title
- Update movie ratings
- Delete movie records
- Sort movies by rating
- Sort movies by release year
- Count total number of movies
- View movies by genre
- Prevent duplicate movie entries
- Case-insensitive movie search
- Basic input validation
- JSON-based data storage

## Movie Data Format

Each movie record contains:

- Title
- Genre
- Release year
- Rating

Example:

```json
{
    "title": "Vikram",
    "genre": "Action",
    "year": 2022,
    "rating": 8.4
}
Technologies Used
Python
JSON
Python Concepts Practiced
File handling
JSON data handling
Lists
Dictionaries
Functions
Loops
Conditional statements
Exception handling
User input
Sorting using lambda functions
Project Structure
movie_project/
|
+-- movie_management.py
+-- movie.json
+-- README.md
Note: movie.json will be created automatically when movie data is saved.

How to Run
Clone the repository:
git clone https://github.com/sivasurya2006/movie_project.git
Go to the project folder:
cd movie_project
Run the Python file:
python movie_management.py
Menu Options
MOVIE MANAGEMENT SYSTEM

1. Add Movie
2. View Movies
3. Search Movie
4. Update Rating
5. Delete Movie
6. Sort Movies by Rating
7. Sort Movies by Release Year
8. Total Movies
9. View Movies by Genre
10. Exit
Example Output
MOVIE MANAGEMENT SYSTEM
1. Add Movie
2. View Movies
3. Search Movie
4. Update Rating
5. Delete Movie
6. Sort Movies by Rating
7. Sort Movies by Release Year
8. Total Movies
9. View Movies by Genre
10. Exit

Enter your choice: 1
Enter movie name: Vikram
Enter genre: Action
Enter release year: 2022
Enter rating: 8.4
Movie added successfully!
Future Improvements
Display movies in a table format
Add rating range validation
Add release year validation
Allow updating movie title, genre, and year
Add search by rating or release year
Improve menu design
Add unit tests
Author
Siva Surya
License
This project is open-source and available for learning and practice purposes.
