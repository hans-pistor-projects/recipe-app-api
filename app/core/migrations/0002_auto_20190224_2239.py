# Generated by Django 2.1.7 on 2019-02-24 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_stafff',
            new_name='is_staff',
        ),
    ]
