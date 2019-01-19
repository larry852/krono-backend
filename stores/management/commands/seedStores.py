from django.core.management.base import BaseCommand
from django_seed.exceptions import SeederCommandError
from django_seed import Seed
from stores.models import Store
from cities.models import City
import random
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Fill database'

    def add_arguments(self, parser):
        parser.add_argument('--number', nargs='?', type=int, default=10, const=10, help='number of each model to seed')

    def handle(self, *args, **options):
        try:
            number = int(options['number'])
        except ValueError:
            raise SeederCommandError('The value of --number must be an integer')

        seeder = Seed.seeder(locale='es_MX')
        seeder.add_entity(Store, number, {
            'name': lambda x: seeder.faker.company(),
            'city': lambda x: random.choice(City.objects.all()),
            'is_active': True,
        })
        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(inserted_pks))

        for store in Store.objects.all():
            for x in range(0, random.randint(0, User.objects.count())):
                store.users.add(random.choice(User.objects.filter(is_staff=False)))
