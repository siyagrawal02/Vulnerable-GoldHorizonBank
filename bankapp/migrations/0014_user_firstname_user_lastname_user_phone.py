# Generated by Django 4.1b1 on 2023-10-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0013_rename_uname_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='0000000000', max_length=10),
        ),
    ]
