# Generated by Django 2.1.4 on 2019-01-07 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0018_auto_20190108_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsuite',
            name='test_case',
        ),
    ]
