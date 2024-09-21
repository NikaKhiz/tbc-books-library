from database_manager import DatabaseManager
from models import engine, Base


def main():
    db = DatabaseManager(engine, Base)
    db.popuate_author_table()
    db.popuate_book_table()


if __name__ == '__main__':
    main()