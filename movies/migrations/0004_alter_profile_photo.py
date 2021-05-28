# Generated by Django 3.2 on 2021-05-28 13:36

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='avatars/default.webp', upload_to=movies.models.user_image_dir),
        ),
    ]