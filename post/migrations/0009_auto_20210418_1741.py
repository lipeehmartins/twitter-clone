# Generated by Django 3.1.4 on 2021-04-18 21:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20210418_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image_path',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
