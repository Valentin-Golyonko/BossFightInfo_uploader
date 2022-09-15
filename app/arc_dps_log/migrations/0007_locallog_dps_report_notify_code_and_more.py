# Generated by Django 4.1.1 on 2022-09-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arc_dps_log", "0006_locallog_bfi_notify_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="locallog",
            name="dps_report_notify_code",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Not uploaded"),
                    (2, "Wrong log name."),
                    (3, "Log exists or in a block list."),
                    (4, "Can not download log."),
                    (5, "Unknown boss (trigger) ID."),
                    (6, "System accept only success golem logs."),
                    (
                        7,
                        "System detected 'Mushroom King's Blessing' (skill reset) button was pressed. This is why it can't accept this log.",
                    ),
                    (
                        8,
                        "You are using old Elite Insights version. Please update it to the latest version (2.45+)!",
                    ),
                    (9, "This log is too old (age more 180 days)!"),
                    (10, "This system can NOT process WvW logs, sorry!"),
                    (11, "This system can NOT process Anonymous logs, sorry!"),
                    (
                        12,
                        "Raid log should be parsed with Elite Insights version 2.45+ because of Emboldened mode.",
                    ),
                    (13, "This system can NOT process Emboldened mode logs, sorry!"),
                    (
                        14,
                        "You can not upload log, because more than 90% Boss health left!",
                    ),
                    (
                        15,
                        "You can not upload log, because fight duration is less than 10 seconds!",
                    ),
                    (16, "Log with the same parameters exists in the system."),
                    (17, "Log file processing error."),
                    (18, "Log uploaded."),
                ],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="locallog",
            name="file_path",
            field=models.CharField(max_length=150),
        ),
    ]