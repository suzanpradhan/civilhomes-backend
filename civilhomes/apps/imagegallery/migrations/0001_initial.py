# Generated by Django 3.1.7 on 2021-05-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='services/')),
                ('image_type', models.IntegerField(choices=[(1, 'Ongoing'), (2, 'Completed')], default=2)),
                ('dimension', models.IntegerField(choices=[(1, '2D'), (2, '3D')], default=1)),
            ],
        ),
    ]
