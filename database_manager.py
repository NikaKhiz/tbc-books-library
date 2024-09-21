from sqlalchemy.orm import sessionmaker


class DatabaseManager():
    def __init__(self, engine, base) -> None:
        base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        