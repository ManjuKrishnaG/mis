# Generated by Django 4.2.7 on 2024-05-07 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0020_table_tablelocation_tabledata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Table',
            new_name='Field_Creation',
        ),
        migrations.RenameModel(
            old_name='TableLocation',
            new_name='Location',
        ),
        migrations.RenameModel(
            old_name='TableData',
            new_name='Title_Creation',
        ),
    ]
