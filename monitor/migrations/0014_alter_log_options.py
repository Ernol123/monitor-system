# Generated by Django 4.2.10 on 2024-02-29 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0013_remove_monitor_status_page_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="log",
            options={
                "ordering": ["-request_date"],
                "verbose_name": "Log",
                "verbose_name_plural": "Logi",
            },
        ),
    ]
