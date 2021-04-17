from django.db import models

# Create your models here.
class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    parent_tweet_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=30)
    content = models.TextField()
    image_path = models.ImageField(upload_to='static/images/', default='')
    created_at = models.DateTimeField(auto_now_add=True)
