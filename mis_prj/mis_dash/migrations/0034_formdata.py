# Generated by Django 4.2.7 on 2024-05-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0033_delete_formdataentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_creation', models.CharField(max_length=255)),
                ('field_name', models.CharField(max_length=255)),
                ('field_value', models.CharField(max_length=255)),
            ],
        ),
    ]
