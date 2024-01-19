# Generated by Django 4.1.2 on 2023-02-10 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus_ambassador',
            fields=[
                ('ca_id', models.CharField(default='x', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('college_name', models.CharField(blank=True, default='IIT Patna', max_length=150, null=True)),
                ('college_city', models.CharField(blank=True, default='Patna', max_length=150, null=True)),
                ('refferal_code', models.CharField(blank=True, max_length=150, null=True)),
                ('age', models.SmallIntegerField(blank=True, default=19, null=True)),
                ('intrests', models.CharField(blank=True, choices=[('intrest1', 'Intrest 1'), ('intrest2', 'Intrest 2'), ('intrest3', 'Intrest 3')], max_length=150, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others'), ('rather_not_say', 'Rather not say')], default='rather_not_say', max_length=20)),
                ('score', models.IntegerField(default=0)),
                ('is_loggedin', models.BooleanField(default=False)),
                ('validation', models.BooleanField(default=False)),
                ('instagram_id', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_id', models.CharField(blank=True, max_length=255, null=True)),
                ('linkdin_id', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_id', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('time_of_registration', models.DateTimeField(auto_now_add=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('anwesha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name': 'Campus Ambassador',
                'verbose_name_plural': 'Campus Ambassadors',
            },
        ),
    ]