# Generated by Django 4.2.7 on 2024-04-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0006_rename_offroll_female_pt_peopletrained_permanentfemale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainedpeople',
            name='form_name',
            field=models.CharField(choices=[('Near miss', 'Near miss'), ('First aid cases', 'First aid cases'), ('Medically treated Injuries (MTI )', 'Medically treated Injuries (MTI )'), (' Restricted Work Case ( RWC)', ' Restricted Work Case ( RWC)'), ('Lost time or reportable Injuries (LTI )', 'Lost time or reportable Injuries (LTI )'), ('Man Power strength', 'Man Power strength')], max_length=100),
        ),
    ]
