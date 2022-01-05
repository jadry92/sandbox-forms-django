# Generated by Django 3.2.8 on 2021-12-20 22:21

import basic_forms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=basic_forms.models.extension_directory_path)),
                ('size', models.PositiveBigIntegerField()),
                ('uploaded', models.DateField(auto_now=True)),
            ],
        ),
    ]
