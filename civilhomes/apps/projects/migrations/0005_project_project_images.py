# Generated by Django 3.1.7 on 2021-05-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagegallery', '0004_delete_imagegallery'),
        ('projects', '0004_auto_20210512_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_images',
            field=models.ManyToManyField(to='imagegallery.Image'),
        ),
    ]
