# Generated by Django 3.2.1 on 2021-07-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_user',
            name='birthday',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='signup_user',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signup_user',
            name='mobile_number',
            field=models.IntegerField(max_length=30),
        ),
    ]
