# Generated by Django 4.2.7 on 2024-05-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0035_title_creation_disable'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='empid',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
