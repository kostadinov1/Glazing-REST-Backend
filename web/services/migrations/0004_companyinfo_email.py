# Generated by Django 4.1 on 2022-09-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_companyinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
