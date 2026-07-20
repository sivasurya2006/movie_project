# Movie Management System

A simple Python command-line project to manage movie records using JSON file storage.

## Description

Movie Management System is a beginner-friendly Python project that allows users to add, view, search, update, delete, sort, and filter movie details. The project stores movie data in a `movie.json` file, so records can be saved and reused after the program runs.

## Features

- Add new movies
- View all movies
- Search movie by title
- Update movie rating
- Delete movie records
- Sort movies by rating
- Sort movies by release year
- Count total movies
- View movies by genre
- Prevent duplicate movie entries
- Store data using JSON

## Movie Details Stored

Each movie record contains:

- Movie title
- Genre
- Release year
- Rating

## Technologies Used

- Python
- JSON

## Concepts Used

- File handling
- JSON data storage
- Lists and dictionaries
- Loops
- Conditional statements
- User input
- Sorting with lambda function

## How to Run

1. Make sure Python is installed on your system.
2. Open Command Prompt or VS Code terminal.
3. Go to the project folder:

```bash
cd C:\Users\FLMXDOC\OneDrive\Desktop\movie_project
```

4. Run the Python file:

```bash
python movie_management.py
```

## Menu Options

```text
1. ADD_MOVIE
2. VIEW_MOVIE
3. SEARCH_MOVIES
4. UPDATE_RATING
5. DELETE_MOVIES
6. SORTED_MOVIES
7. SORTED_YEAR
8. TOTAL_MOVIES
9. VIEW_MOVIES_BY_GENRE
10. PREVENT_DUPLICATE_MOVIE
```

## File Structure

```text
movie_project/
|
+-- movie_management.py
+-- movie.json
+-- README.md
```

## Example Movie Data

```json
[
    {
        "title": "Vikram",
        "genre": "Action",
        "year": 2022,
        "rating": 8.4
    }
]
```

## Future Improvements

- Improve input validation
- Add case-insensitive movie search
- Display movies in table format
- Add separate functions for each feature
- Add exit option
- Improve error handling

## Author

Siva Surya

## Note

This is a beginner-level Python mini project created for practicing file handling, JSON storage, and CRUD operations.
