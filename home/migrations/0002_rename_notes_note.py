# Generated by Django 5.1.2 on 2024-10-17 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]