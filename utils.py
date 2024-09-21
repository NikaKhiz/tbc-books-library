from faker import Faker
from datetime import datetime, timedelta
from models import Author

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
