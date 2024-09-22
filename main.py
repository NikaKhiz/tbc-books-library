from database_manager import DatabaseManager
from models import engine, Base


def main():
    db = DatabaseManager(engine, Base)
    db.populate_author_table()
    db.populate_book_table()
    db.populate_author_book_table()

    print(f'books with most pages {db.books_with_most_pages()}')
    print(f'average of pages is : {db.avg_of_pages()}')
    print(f'youngest authors : {db.youngest_authors()}')
    print(f'authors without books : {db.authors_without_books()}')
    print(f'authors with more then three book : {db.authors_with_more_then_three_book()}')

    # Demonstrates many to many relationship 
    print(f'books with several authors : {db.books_with_many_authors()}')

if __name__ == '__main__':
    main()