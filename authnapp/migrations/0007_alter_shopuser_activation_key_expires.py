# Generated by Django 3.2.11 on 2022-02-16 19:52

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0006_alter_shopuser_activation_key_expires"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 18, 19, 52, 21, 426206, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
