# Generated by Django 4.0.3 on 2022-03-17 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Move',
            new_name='Movie',
        ),
    ]