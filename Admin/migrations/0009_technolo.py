# Generated by Django 5.0 on 2024-03-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_collaborations_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='technolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_icon', models.CharField(max_length=188)),
            ],
        ),
    ]
