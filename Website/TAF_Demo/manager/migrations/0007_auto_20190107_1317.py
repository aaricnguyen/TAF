# Generated by Django 2.1.4 on 2019-01-07 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_amenity_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='amenities',
        ),
        migrations.DeleteModel(
            name='Amenity',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
