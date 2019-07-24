from django.db import models

# Create your models here.


class Arts(models.Model):
    txt = models.TextField()
    title = models.CharField(max_length=255)
    user_id = models.IntegerField()
    date = models.DateField()


class Comments(models.Model):
    comments = models.TextField()
    user_id = models.IntegerField()
    art_id = models.IntegerField()


class FavArt(models.Model):
    art_id = models.IntegerField()
    user_id = models.IntegerField()
