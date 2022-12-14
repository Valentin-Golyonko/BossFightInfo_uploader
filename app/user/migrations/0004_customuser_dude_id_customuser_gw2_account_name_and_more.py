# Generated by Django 4.0.7 on 2022-09-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_customuser_auth_str"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="dude_id",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="customuser",
            name="gw2_account_name",
            field=models.CharField(
                blank=True, default="", max_length=50, verbose_name="GW2 Account"
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_email_confirmed",
            field=models.BooleanField(default=False),
        ),
    ]
