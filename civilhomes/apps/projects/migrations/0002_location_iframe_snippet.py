# Generated by Django 3.1.7 on 2021-04-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='iframe_snippet',
            field=models.TextField(blank=True, null=True),
        ),
    ]