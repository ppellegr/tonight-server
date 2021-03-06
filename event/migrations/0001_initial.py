# Generated by Django 2.2 on 2020-03-04 14:27

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('max_radius', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('like_number', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('venue_name', models.CharField(max_length=200)),
                ('venue_adress', models.CharField(max_length=200)),
                ('postal_code', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=17)),
                ('free_of_charge', models.NullBooleanField()),
                ('profiles', models.ManyToManyField(to='event.Profile')),
            ],
        ),
    ]
