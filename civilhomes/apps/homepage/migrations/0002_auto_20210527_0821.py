# Generated by Django 3.1.7 on 2021-05-27 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosection',
            name='videoTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]