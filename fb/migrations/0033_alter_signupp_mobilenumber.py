# Generated by Django 3.2.1 on 2021-07-29 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0032_alter_signupp_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupp',
            name='mobilenumber',
            field=models.IntegerField(max_length=60),
        ),
    ]
