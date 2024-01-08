from django.db import models
from faker import Faker
import random

fake = Faker()

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"

    @classmethod
    def generate_items(cls, num_items=100):
        items = []
        for _ in range(num_items):
            item = cls(
                name=fake.word(),
                description=fake.text(),
                price=random.uniform(5.0, 100.0)
            )
            items.append(item)
        cls.objects.bulk_create(items)
