import csv
from pathlib import Path

from django.db.models.signals import post_save
from django.dispatch import receiver

from bf_task.compute.models import UserCSVProvidedFile, ComputedCSVCalculation
from bf_task.settings import MEDIA_ROOT


@receiver(post_save, sender=UserCSVProvidedFile)
def calc_and_save(sender, instance, created, **kwargs):
    if created:
        p = Path(MEDIA_ROOT)
        file_name = instance.file_reference
        location = p / f'{file_name}'
        with open(location, newline='') as csvfile:
            total_sum = 0
            csv_reader = csv.reader(csvfile, delimiter='|')
            next(csv_reader)

            for row in csv_reader:
                A = float(row[0])
                O = row[1].strip()
                B = float(row[2])

                if O == '+':
                    result = A + B
                elif O == '-':
                    result = A - B
                elif O == '*':
                    result = A * B
                else:
                    result = A / B

                total_sum += result
            print(total_sum)

        ComputedCSVCalculation.objects.create(
            csv_file=instance,
            result= total_sum,
        )