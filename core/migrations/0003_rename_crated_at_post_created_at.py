# Generated by Django 4.0.6 on 2022-07-22 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='crated_at',
            new_name='created_at',
        ),
    ]
