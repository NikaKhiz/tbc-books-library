from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import func
import json
from utils import *
from models import Author, AuthorBook


class DatabaseManager():
    def __init__(self, engine, base) -> None:
        base.metadata.drop_all(engine)
        base.metadata.create_all(engine)
        
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()


    def populate_author_table(self):
        authors = [generate_random_author() for _ in range(500)]
        self.session.add_all(authors)
        self.session.commit()


    def populate_book_table(self):
        authors = self.session.query(Author.id, Author.birth_date).all()
        books = [generate_random_book(authors) for _ in range(1000)]
        self.session.add_all(books)
        self.session.commit()


    
    def populate_author_book_table(self):
        authors = self.session.query(Author).all()
        books = self.session.query(Book).all()

        author_books = []

        # generate random number of authors for particular book
        for book in books:
            
            num_authors = random.randint(2, 4) 
            selected_authors = random.sample(authors, min(num_authors, len(authors)))

            for author in selected_authors:
                author_books.append(AuthorBook(author_id=author.id, book_id=book.id))

        self.session.add_all(author_books)
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
    

    def authors_with_more_then_three_book(self):
        authors = (
        self.session.query(
            Author.id,
            Author.first_name,
            Author.last_name,
            func.count(Book.id).label('book_count')
        )
        .join(Book, Author.id == Book.author_id)
        .group_by(Author.id)
        .having(func.count(Book.id) > 3)
        .limit(5)
        .all()
        )

        authors_list = [
            {
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'book_count': author.book_count
            }
            for author in authors
        ]

        return json.dumps(authors_list, indent=4)

    
    def books_with_many_authors(self):
        books_with_authors = self.session.query(Book).options(joinedload(Book.author)).all()
        
        books_list = [
                {
                    'id': book.id,
                    'title': book.title,
                    'author': [
                        {
                            'first_name': author.first_name,
                            'last_name': author.last_name
                        } for author in book.author
                    ]
                }
                for book in books_with_authors if len(book.author) > 1 
        ]
        
        random_books = random.sample(books_list, min(5, len(books_list)))

        return json.dumps(random_books, indent=4)


       




