# Generated by Django 4.2.7 on 2024-05-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0024_remove_location_table_names_location_division_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field_creation',
            name='field',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]