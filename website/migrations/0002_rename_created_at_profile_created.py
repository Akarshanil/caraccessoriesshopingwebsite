# Generated by Django 4.2.4 on 2023-08-07 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created_at',
            new_name='created',
        ),
    ]