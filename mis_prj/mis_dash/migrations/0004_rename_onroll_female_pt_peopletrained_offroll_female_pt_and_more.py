# Generated by Django 4.2.7 on 2024-04-23 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0003_rename_permanent_female_count_peopletrained_onroll_female_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peopletrained',
            old_name='onroll_female_pt',
            new_name='offroll_female_pt',
        ),
        migrations.RenameField(
            model_name='peopletrained',
            old_name='onroll_male',
            new_name='offroll_male',
        ),
    ]