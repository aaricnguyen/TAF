# Generated by Django 2.1.4 on 2019-01-08 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0026_testsuite_test_case'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsuite',
            name='test_case',
        ),
    ]
