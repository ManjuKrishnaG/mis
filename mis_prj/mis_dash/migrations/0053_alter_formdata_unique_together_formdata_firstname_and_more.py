# Generated by Django 5.0 on 2024-05-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0052_rename_uploaded_at_attachment_uploaded_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='formdata',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='formdata',
            name='firstname',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='formdata',
            name='form_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='field_creation',
            name='field',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='title_creation',
            name='title_creation',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
