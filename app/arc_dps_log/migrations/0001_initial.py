# Generated by Django 4.0.7 on 2022-09-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LocalLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_name", models.CharField(max_length=30)),
                ("file_path", models.CharField(max_length=1000)),
                (
                    "dps_report_status",
                    models.PositiveIntegerField(
                        choices=[(1, "ok"), (2, "pending"), (3, "error")],
                        db_index=True,
                        default=2,
                    ),
                ),
                ("dps_report_name", models.CharField(max_length=50)),
                (
                    "bfi_status",
                    models.PositiveIntegerField(
                        choices=[(1, "ok"), (2, "pending"), (3, "error")],
                        db_index=True,
                        default=2,
                    ),
                ),
                (
                    "bfi_fight_id",
                    models.PositiveBigIntegerField(blank=True, default=None, null=True),
                ),
            ],
        ),
    ]
