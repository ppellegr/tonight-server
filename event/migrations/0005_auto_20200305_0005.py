# Generated by Django 2.2 on 2020-03-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20200305_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
