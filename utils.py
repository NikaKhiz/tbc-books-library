from faker import Faker
from datetime import datetime, timedelta
import random
from models import Author, Book

fake = Faker()


def generate_random_author():
    today = datetime.now().date()
    min_birth_date = today - timedelta(days=365 * 18)
    first_name = fake.first_name()
    last_name = fake.last_name()
    country = fake.city()
    
    birth_date = fake.date_of_birth(maximum_age=100)
    # ensure that birth date is no later than the min_birth_date
    while birth_date > min_birth_date:
        birth_date = fake.date_of_birth(maximum_age=100)
    
    return Author(first_name = first_name, last_name = last_name, country = country, birth_date = birth_date)



def generate_random_book(authors):
    # get author birth date to ensure author wrote book after 18
    author_id, birth_date = random.choice(authors)
    
    min_release_year = birth_date.year + 18
    current_year = datetime.now().year

    if min_release_year > current_year:
        min_release_year = current_year

    release_year = random.randint(min_release_year, current_year)
    release_month = random.randint(1, 12)
    release_day = random.randint(1, 28)
    
    release_date = datetime(release_year, release_month, release_day)
    title = fake.catch_phrase() 
    category = fake.word()
      
    # ensure that category length is long enough
    while len(category) < 4:
        category = fake.word()
        
    pages = random.randint(50, 500)

    return Book(author_id = author_id, title = title , category = category, pages = pages, release_date = release_date)