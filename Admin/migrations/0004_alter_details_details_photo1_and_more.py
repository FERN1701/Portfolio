# Generated by Django 5.0 on 2024-03-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_details_cvfile_details_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Details_photo1',
            field=models.FileField(null=True, upload_to='Details Photos'),
        ),
        migrations.AlterField(
            model_name='details',
            name='Details_photo2',
            field=models.FileField(null=True, upload_to='Details Photos'),
        ),
        migrations.AlterField(
            model_name='details',
            name='portfolio_profile',
            field=models.FileField(null=True, upload_to='Portfolio Profile'),
        ),
        migrations.AlterField(
            model_name='details',
            name='youtube',
            field=models.CharField(max_length=1888, null=True),
        ),
    ]