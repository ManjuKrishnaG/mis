# Generated by Django 4.2.7 on 2024-05-02 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0017_peopletrained_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopletrained',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
