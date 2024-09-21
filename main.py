from database_manager import DatabaseManager
from models import engine, Base


def main():
    db = DatabaseManager(engine, Base)
    db.popuate_author_table()
    db.popuate_book_table()

    print(f'books with most pages {db.books_with_most_pages()}')
    print(f'average of pages is : {db.avg_of_pages()}')
    print(f'youngest authors : {db.youngest_authors()}')
    print(f'authors without books : {db.authors_without_books()}')
    print(f'authors with more then three book : {db.authors_with_more_then_three_book()}')

if __name__ == '__main__':
    main()