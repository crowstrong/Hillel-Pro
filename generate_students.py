from sys import argv
import random
import pandas as pd
from faker import Faker

quantity = int(argv[1])

fake_instance = Faker('uk_UA')

students_data: list = [
    {
        'First_name': fake_instance.first_name(),
        'Last_name': fake_instance.last_name(),
        'Email': fake_instance.unique.email(),
        'Password': fake_instance.password(length=random.randint(10, 20)),
        'Birthday': str(fake_instance.date_of_birth(minimum_age=18, maximum_age=28))
    } for data in range(quantity)
]
df = pd.DataFrame(students_data)
df.to_csv('students_data.csv', index=False)

print(df)
