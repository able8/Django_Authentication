# Generated by Django 2.0.5 on 2018-08-17 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commonuserform',
            old_name='nikename',
            new_name='nickname',
        ),
    ]
