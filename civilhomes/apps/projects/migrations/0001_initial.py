# Generated by Django 3.2.4 on 2021-07-15 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imagegallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=10)),
                ('iframe_snippet', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'Not Started'), (2, 'Ongoing'), (3, 'Completed'), (4, 'On Hold')], default=1)),
                ('brochure_url', models.FileField(upload_to='brochures/')),
                ('amenities', models.ManyToManyField(to='projects.Amenitie')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.location')),
                ('project_images', models.ManyToManyField(to='imagegallery.Image')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_url', models.FileField(upload_to='project_sheet_files/')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.info')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExtrasCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_infos',
            field=models.ManyToManyField(to='projects.ProjectInfo'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectplan'),
        ),
    ]
