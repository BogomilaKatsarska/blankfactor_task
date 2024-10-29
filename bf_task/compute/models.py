from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class UserCSVProvidedFile(models.Model):
    MAX_NAME_OF_REQUEST_LEN = 500

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='csv_files',
        null=False,
        blank=False,
    )
    name_of_request = models.CharField(
        max_length=MAX_NAME_OF_REQUEST_LEN,
        null=False,
        blank=False,
    )
    file_reference = models.FileField(
        upload_to='csv_files/',
        null=False,
        blank=False,
    )
    def __str__(self):
        return f'{self.name_of_request} request has been created by {self.user}'


class ComputedCSVCalculation(models.Model):
    csv_file = models.OneToOneField(
        UserCSVProvidedFile,
        on_delete=models.CASCADE,
        related_name='computed_csv_calculation',
        null=False,
        blank=False,
    )
    result = models.FloatField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'({self.result}) -> the result for {self.csv_file} '