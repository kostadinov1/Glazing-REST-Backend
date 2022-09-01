import uuid
from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=50, default='Unknown', blank=True, null=True,)
    cover_image = models.ImageField(upload_to='album_covers', blank=True, null=True)
    description = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def scramble_uploaded_filename(instance, filename):
    extension = filename.split('.')[-1]
    return '{}.{}'.format(uuid.uuid4(), extension)


class Image(models.Model):
    image_file = models.ImageField(upload_to=scramble_uploaded_filename)
    created_on = models.DateTimeField(auto_now_add=True)
    album_id = models.ForeignKey(Album, related_name='image_set', on_delete=models.CASCADE,)
