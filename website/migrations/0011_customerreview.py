# Generated by Django 4.2.4 on 2023-08-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_rename_address_contsave_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discription', models.CharField(max_length=255)),
            ],
        ),
    ]
