# Generated by Django 3.2.1 on 2021-07-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0017_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='birthday',
            field=models.CharField(max_length=50),
        ),
    ]
