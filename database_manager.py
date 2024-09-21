from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import json
from utils import *
from models import Author 


class DatabaseManager():
    def __init__(self, engine, base) -> None:
        base.metadata.drop_all(engine)
        base.metadata.create_all(engine)
        
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()


    def popuate_author_table(self):
        authors = [generate_random_author() for _ in range(500)]
        self.session.add_all(authors)
        self.session.commit()


    def popuate_book_table(self):
        authors = self.session.query(Author.id, Author.birth_date).all()
        books = [generate_random_book(authors) for _ in range(1000)]
        self.session.add_all(books)
        self.session.commit()


    def books_with_most_pages(self):
        # check for largest num of pages from book, for filtering
        max_pages = self.session.query(func.max(Book.pages)).scalar()
        books = self.session.query(Book).filter(Book.pages == max_pages).all()

        books_list = [
            {
                'id': book.id,
                'title': book.title,
                'pages': book.pages,
                'release_date': book.release_date.isoformat(),
                'author_id': book.author_id
            }
            for book in books
        ]
        
        return json.dumps(books_list, indent=4)
    

    def avg_of_pages(self):
        average = self.session.query(func.avg(Book.pages)).scalar()

        return average
    

    def youngest_authors(self):
        max_birth_date = self.session.query(func.max(Author.birth_date)).scalar()
        authors = self.session.query(Author).filter(Author.birth_date == max_birth_date).all()

        authors_list = [
            {
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'country': author.country,
                'birth_date': author.birth_date.isoformat()
            }
            for author in authors
        ]

        return json.dumps(authors_list, indent=4)  


    def authors_without_books(self):
        authors = (
            self.session.query(Author)
            .outerjoin(Book)
            .filter(Book.id.is_(None))
            .with_entities(Author.id, Author.first_name, Author.last_name)  
            .all()
        )

        authors_list = [
            {
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name
            }
            for author in authors
        ]

        return json.dumps(authors_list, indent=4)




