# Generated by Django 4.2.7 on 2024-04-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0004_rename_onroll_female_pt_peopletrained_offroll_female_pt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peopletrained',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]