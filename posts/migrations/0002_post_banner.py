# Generated by Django 5.0.6 on 2024-06-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(default='fallback.png', upload_to='banners/'),
        ),
    ]
