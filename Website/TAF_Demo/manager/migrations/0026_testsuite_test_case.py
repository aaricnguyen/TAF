# Generated by Django 2.1.4 on 2019-01-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0025_remove_testsuite_test_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsuite',
            name='test_case',
            field=models.ManyToManyField(blank=True, to='manager.TestCase'),
        ),
    ]
