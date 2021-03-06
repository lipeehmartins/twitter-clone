# Generated by Django 3.1.4 on 2020-12-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_tweet_id', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('image_path', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
