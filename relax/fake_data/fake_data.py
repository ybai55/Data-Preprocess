from faker import Faker
from faker.providers import BaseProvider
import random


class CustomProvider(BaseProvider):
    # TODO: read JSON to generate correspond content
    def destination(self):
        destinations = ['NY', 'CO', 'CA', 'TX', 'RI']

        # We select a random destination from the list and return it
        return random.choice(destinations)


fake = Faker(['zh-CN'])
print(fake.name())
print(fake.address())
print(fake.profile())
fake.add_provider(CustomProvider)
print(fake.destination())
