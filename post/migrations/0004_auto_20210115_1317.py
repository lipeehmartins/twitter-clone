# Generated by Django 3.1.4 on 2021-01-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210114_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image_path',
            field=models.ImageField(default='', upload_to='static/images/'),
        ),
    ]
