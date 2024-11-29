from faker import Faker
fake = Faker()


def generate_user_data():
    user_data = {
        "email": f'test1488{fake.email()}',
        "password": fake.password(),
        "name": f'test1488{fake.name()}'
    }
    return user_data