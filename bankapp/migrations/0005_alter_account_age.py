# Generated by Django 4.1 on 2022-10-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_account_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
