# Generated by Django 4.1.5 on 2023-01-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='city_poster')),
                ('venue', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('contacts', models.JSONField()),
                ('register_link', models.URLField()),
                ('rulebook', models.URLField()),
                ('description', models.TextField()),
                ('events', models.JSONField()),
            ],
        ),
    ]
