from django.core.management.base import BaseCommand
from django_seed.exceptions import SeederCommandError
from django_seed import Seed
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
        seeder.add_entity(User, number, {
            'is_staff': False,
            'is_superuser': False,
            'is_active': True,
        })
        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(inserted_pks))
