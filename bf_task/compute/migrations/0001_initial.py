# Generated by Django 4.2.16 on 2024-10-28 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCSVProvidedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_request', models.CharField(max_length=500)),
                ('file_reference', models.FileField(upload_to='csv_files/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csv_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
