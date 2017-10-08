from django.core.management.base import BaseCommand, CommandError
from accelerometer.models import Position
from django.utils import timezone
from django.db.models.signals import post_save
import random



class Command(BaseCommand):
    help = 'Load junk data into the Position model'

    def handle(self, *args, **options):
        num = 101
        # Load in junk
        for x in range(1, num):
            instance = Position.objects.create(
                timestamp=timezone.now(),
                x=random.choice(range(1, 101)),
                y=random.choice(range(1, 101)),
                z=random.choice(range(1, 101)),
            )
            post_save.send(Position, instance=instance, created=True)
