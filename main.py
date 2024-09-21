from database_manager import DatabaseManager
from models import engine, Base


def main():
    db = DatabaseManager(engine, Base)
    db.popuate_author_table()
    db.popuate_book_table()

    print(f'books with most pages {db.books_with_most_pages()}')

if __name__ == '__main__':
    main()