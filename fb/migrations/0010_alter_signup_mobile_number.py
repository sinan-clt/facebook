# Generated by Django 3.2.1 on 2021-07-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0009_auto_20210729_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='mobile_number',
            field=models.CharField(max_length=30),
        ),
    ]
