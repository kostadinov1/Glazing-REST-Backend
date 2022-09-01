# Generated by Django 4.1 on 2022-09-01 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_album_cover_image_album_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='album_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_set', to='gallery.album'),
        ),
    ]
