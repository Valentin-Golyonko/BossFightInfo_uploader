# Generated by Django 4.0.7 on 2022-09-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("arc_dps_log", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="locallog",
            name="file_name",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
