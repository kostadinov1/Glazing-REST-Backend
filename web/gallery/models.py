from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=50, default='Unknown', blank=True, null=True,)
    created_on = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image_file = models.ImageField(upload_to='')
    created_on = models.DateTimeField(auto_now_add=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE,)
