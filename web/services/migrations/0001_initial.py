# Generated by Django 4.1 on 2022-11-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('address', models.TextField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.TextField(blank=True, max_length=300, null=True)),
                ('mobile_phone', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('work_duration', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='service_images')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
