
import pandas as pd

# Create a DataFrame with the provided data
data = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
             108],
    'Title': [
        'To Kill a Mockingbird', '1984', 'The Lord of the Rings', 'The Catcher in the Rye', 'The Great Gatsby',
        'The Lion, the Witch, and the Wardrobe', 'Lord of the Flies', 'Animal Farm', 'Catch-22', 'The Grapes of Wrath',
        'The Kite Runner', 'The Hitchhiker\'s Guide to the Galaxy', 'The Book Thief', 'The Color Purple',
        'The Time Traveler\'s Wife', 'The Count of Monte Cristo', 'The Secret Life of Bees', 'The Handmaid\'s Tale',
        'The Fault in Our Stars', 'The Picture of Dorian Gray',
        'Harry Potter and the Sorcerer’s Stone (Philosopher’s Stone)',
        'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Prisoner of Azkaban',
        'Harry Potter and the Goblet of Fire',
        'Harry Potter and the Order of the Phoenix', 'Harry Potter and the Half-Blood Prince',
        'Harry Potter and the Deathly Hallows',
        'Harry Potter and the Cursed Child'
    ],
    'Author': [
        'Harper Lee', 'George Orwell', 'J.R.R. Tolkien', 'J.D. Salinger', 'F. Scott Fitzgerald',
        'C.S. Lewis', 'William Golding', 'George Orwell', 'Joseph Heller', 'John Steinbeck',
        'Khaled Hosseini', 'Douglas Adams', 'Markus Zusak', 'Alice Walker', 'Audrey Niffenegger',
        'Alexandre Dumas', 'Sue Monk Kidd', 'Margaret Atwood', 'John Green', 'Oscar Wilde', 'J.K. Rowling',
        'J.K. Rowling', 'J.K. Rowling', 'J.K. Rowling', 'J.K. Rowling', 'J.K. Rowling', 'J.K. Rowling', 'J.K. Rowling'
    ],
    'Genre': [
        'Fiction', 'Fiction', 'Fantasy', 'Fiction', 'Fiction',
        'Fantasy', 'Fiction', 'Fiction', 'Fiction', 'Fiction',
        'Fiction', 'Science Fiction', 'Historical Fiction', 'Fiction', 'Fantasy',
        'Historical Fiction', 'Fiction', 'Dystopian', 'Young Adult', 'Gothic', 'Fantasy',
        'Fantasy', 'Fantasy', 'Fantasy', 'Fantasy', 'Fantasy', 'Fantasy', 'Fantasy'
    ],
    '(Publication Year)': [
        1960, 1949, '1954-1955', 1951, 1925,
        1950, 1954, 1945, 1961, 1939,
        2003, 1979, 2005, 1982, 2003,
        1844, 2002, 1985, 2012, 1890, 1997,
        1998, 1999, 2000, 2003, 2005, 2007, 2016
    ],
    'Pages': [
        281, 328, 1178, 277, 180,
        206, 224, 112, 453, 464,
        371, 193, 552, 295, 546,
        1276, 336, 311, 313, 254, 309,
        341, 435, 734, 870, 652, 759, 343
    ],
    'Description': [
        'A novel set in the American South during the 1930s, focusing on themes of racial injustice and moral growth.',
        'A dystopian novel depicting a totalitarian society under constant surveillance.',
        'An epic fantasy trilogy about the quest to destroy a powerful ring.',
        'A story about teenage rebellion and alienation, narrated by the iconic Holden Caulfield.',
        'A critique of the American Dream set in the Roaring Twenties.',
        'A fantasy novel about four children who discover a magical world inside a wardrobe.',
        'A novel about a group of boys stranded on an uninhabited island and their descent into savagery.',
        'An allegorical novella critiquing totalitarian regimes through the story of a farm animal rebellion.',
        'A satirical novel about the absurdities of war and bureaucracy.',
        'A novel about the struggles of a poor family during the Great Depression.',
        'A story of friendship and redemption set against the backdrop of a changing Afghanistan.',
        'A comedic science fiction series about the adventures of Arthur Dent in space.',
        'A historical novel narrated by Death, set in Nazi Germany.',
        'A novel about the life of African American women in the early 20th century American South.',
        'A love story about a man with a genetic disorder that causes him to time travel unpredictably.',
        'A tale of an innocent man wrongfully imprisoned and his quest for revenge.',
        'A coming-of-age story set in the 1960s American South, focusing on themes of race and family.',
        'A dystopian novel about a theocratic society where women are subjugated.',
        'A young adult novel about two teenagers with cancer who fall in love.',
        'A novel about a man who remains young and beautiful while his portrait ages and reflects his moral corruption.',
        'Harry discovers he is a wizard on his eleventh birthday and attends Hogwarts School of Witchcraft and Wizardry, where he learns about his past and his connection to the dark wizard Voldemort.',
        'Harry returns to Hogwarts for his second year and discovers a hidden chamber within the school, unleashing a monster that petrifies students.',
        'In his third year, Harry learns about Sirius Black, an escaped prisoner who is believed to be after him, and uncovers secrets about his parents’ past.',
        'Harry is unexpectedly entered into the Triwizard Tournament, a dangerous magical competition, and faces challenges that test his courage and skills.',
        'Harry’s fifth year at Hogwarts is marked by the return of Voldemort, the formation of the Order of the Phoenix, and a battle at the Ministry of Magic.',
        'In his sixth year, Harry discovers a mysterious book belonging to the “Half-Blood Prince” and learns more about Voldemort’s past and his Horcruxes.',
        'The final book follows Harry, Ron, and Hermione as they leave Hogwarts to find and destroy Voldemort’s Horcruxes, leading to a final battle at the school.',
        'A play set nineteen years after the events of the original series, focusing on Harry’s son Albus and his struggles with his family’s legacy.'
    ]
}

books_df = pd.DataFrame(data)


def search_book(title):
    book = books_df[books_df['Title'].str.contains(title, case=False, na=False)]
    if not book.empty:
        return book[['Title', 'Author', 'Genre', '(Publication Year)', 'Pages', 'Description']]
    else:
        return "Book not found."


def search_books_by_author(author):
    books = books_df[books_df['Author'].str.contains(author, case=False, na=False)]
    if not books.empty:
        return books[['Title', 'Author', 'Genre', '(Publication Year)', 'Pages', 'Description']]
    else:
        return "No books found by this author."


def get_recommendations(title):
    book = books_df[books_df['Title'].str.contains(title, case=False, na=False)]
    if book.empty:
        return "Book not found."

    genre = book.iloc[0]['Genre']
    recommendations = books_df[books_df['Genre'] == genre]
    recommendations = recommendations[recommendations['Title'] != book.iloc[0]['Title']]

    return recommendations[['Title', 'Author']]


def display_book_info_and_recommendations(title=None, author=None):
    if title:
        book_info = search_book(title)
        if isinstance(book_info, str):
            print(book_info)
        else:
            print("Book Information:")
            print(book_info)

            # Ask the user if they want recommendations
            user_input = input("Would you like book recommendations based on this book? (yes/no): ").strip().lower()
            if user_input == 'yes':
                print("\nRecommended Books:")
                recommendations = get_recommendations(title)
                print(recommendations)
            else:
                print("No recommendations will be provided.")
    elif author:
        books_info = search_books_by_author(author)
        if isinstance(books_info, str):
            print(books_info)
        else:
            print("Books by Author:")
            print(books_info)


# Example usage
search_type = input("Do you want to search by title or author? (title/author): ").strip().lower()
if search_type == 'title':
    book_title = input("Enter the title of the book you are looking for: ")
    display_book_info_and_recommendations(title=book_title)
elif search_type == 'author':
    author_name = input("Enter the name of the author you are looking for: ")
    display_book_info_and_recommendations(author=author_name)
else:
    print("Invalid input. Please enter 'title' or 'author'.")
