# Generated by Django 4.2.7 on 2024-04-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0009_achievements_for_the_month_incidents_manhours_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_permit_issued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_permit_issue', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='commonone',
            options={'verbose_name': 'Training Data', 'verbose_name_plural': 'Training Data'},
        ),
    ]