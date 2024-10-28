# Book Search and Recommendation System

This Python script implements a simple book search and recommendation system using a pandas DataFrame to store and manage book information. Users can search for books by title or author and receive detailed information, including recommendations based on the book's genre.

## Features

- **Search by Title**: Look up book details using a title query.
- **Search by Author**: Retrieve a list of books by a specific author.
- **Recommendations**: Get book recommendations based on the genre of the searched book.
- **User Interaction**: Interactive command-line interface for user inputs and responses.

## Data Structure

The system uses a pandas DataFrame containing the following columns:

- **Rank**: Ranking of the book.
- **Title**: Title of the book.
- **Author**: Author of the book.
- **Genre**: Genre of the book.
- **(Publication Year)**: Year the book was published.
- **Pages**: Number of pages in the book.
- **Description**: Brief description of the book.

## Usage

1. Run the script in a Python environment.
2. Choose to search by **title** or **author** when prompted.
3. Input the desired title or author name to see results.

## Example

```python
search_type = input("Do you want to search by title or author? (title/author): ")
if search_type == 'title':
    book_title = input("Enter the title of the book you are looking for: ")
    display_book_info_and_recommendations(title=book_title)
elif search_type == 'author':
    author_name = input("Enter the name of the author you are looking for: ")
    display_book_info_and_recommendations(author=author_name)
```

## Requirements

- Python 3.x
- pandas library

## Future Enhancements

- Implement a graphical user interface (GUI) for better user experience.
- Expand the dataset with more books and authors.
- Add functionality to allow users to add or remove books from the collection.

