# Generated by Django 4.2.7 on 2024-05-09 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0028_formdataentry_delete_dynamicinputmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title_creation',
            old_name='fields',
            new_name='field_name',
        ),
        migrations.RenameField(
            model_name='title_creation',
            old_name='title',
            new_name='title_creation',
        ),
    ]
