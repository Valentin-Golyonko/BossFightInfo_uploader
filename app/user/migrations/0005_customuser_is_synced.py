# Generated by Django 4.1.1 on 2022-09-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_dude_id_customuser_gw2_account_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_synced',
            field=models.BooleanField(default=False),
        ),
    ]