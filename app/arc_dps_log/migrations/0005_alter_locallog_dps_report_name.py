# Generated by Django 4.0.7 on 2022-09-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ("arc_dps_log", "0004_alter_locallog_options_locallog_file_time_and_more"),
]

    operations = [
        migrations.AlterField(
            model_name="locallog",
            name="dps_report_name",
            field=models.CharField(default="", max_length=50),
        ),
    ]
