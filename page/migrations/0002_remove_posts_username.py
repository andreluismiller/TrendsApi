# Generated by Django 4.2 on 2023-04-07 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='username',
        ),
    ]
