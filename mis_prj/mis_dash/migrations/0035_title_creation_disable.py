# Generated by Django 4.2.7 on 2024-05-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0034_formdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='title_creation',
            name='disable',
            field=models.BooleanField(default=False),
        ),
    ]
