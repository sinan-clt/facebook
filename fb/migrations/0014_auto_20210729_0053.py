# Generated by Django 3.2.1 on 2021-07-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0013_auto_20210729_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='signup',
            name='mobilenumber',
            field=models.IntegerField(),
        ),
    ]
