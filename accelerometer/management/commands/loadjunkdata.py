from django.core.management.base import BaseCommand, CommandError
from accelerometer.models import Position
from django.utils import timezone
import random



class Command(BaseCommand):
    help = 'Load junk data into the Position model'

    def handle(self, *args, **options):
        # Flush what's there
        Position.objects.all().delete()
        # Load in junk
        for x in range(1, 101):
            Position.objects.create(
                timestamp=timezone.now(),
                x=random.choice(range(1, 101)),
                y=random.choice(range(1, 101)),
                z=random.choice(range(1, 101)),
            )
