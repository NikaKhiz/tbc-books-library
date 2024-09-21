from sqlalchemy.orm import sessionmaker
from utils import *


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
        
