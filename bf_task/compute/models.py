from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class CSVFile(models.Model):
    MAX_NAME_OF_REQUEST_LEN = 500

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
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