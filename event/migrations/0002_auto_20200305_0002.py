# Generated by Django 2.2 on 2020-03-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='last_update',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pic_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='record_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='free_of_charge',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=17, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='like_number',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=17, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='postal_code',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='profiles',
            field=models.ManyToManyField(null=True, to='event.Profile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue_adress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
