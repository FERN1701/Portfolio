# Generated by Django 5.0 on 2024-03-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_rename_details_photo_details_details_photo1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='cvfile',
            field=models.FileField(default=1, upload_to='Curriculum vitae'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='youtube',
            field=models.CharField(default=1, max_length=1888),
            preserve_default=False,
        ),
    ]
