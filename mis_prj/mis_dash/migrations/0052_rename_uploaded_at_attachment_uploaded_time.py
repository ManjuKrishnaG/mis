# Generated by Django 4.2.7 on 2024-05-17 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0051_attachment_empid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='uploaded_at',
            new_name='uploaded_time',
        ),
    ]
