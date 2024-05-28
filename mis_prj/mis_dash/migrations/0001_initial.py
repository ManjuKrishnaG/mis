# Generated by Django 4.2.7 on 2024-04-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleTrained',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('permanent_male_count', models.IntegerField(default=0)),
                ('permanent_female_count', models.IntegerField(default=0)),
                ('temporary_male_count', models.IntegerField(default=0)),
                ('temporary_female_count', models.IntegerField(default=0)),
            ],
        ),
    ]
