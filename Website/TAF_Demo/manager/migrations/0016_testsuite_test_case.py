# Generated by Django 2.1.4 on 2019-01-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_auto_20190108_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsuite',
            name='test_case',
            field=models.ManyToManyField(blank=True, to='manager.TestCase'),
        ),
    ]
