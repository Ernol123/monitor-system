# Generated by Django 5.0.2 on 2024-03-08 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0025_alter_monitor_days_before_exp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monitor",
            name="monitor_type",
            field=models.CharField(
                choices=[
                    ("http_request", "Zapytanie HTTP"),
                    ("ping", "Ping"),
                    ("cron_job", "Crone Job"),
                ],
                default="http_request",
                max_length=15,
                verbose_name="Typ monitorowania",
            ),
        ),
        migrations.CreateModel(
            name="ApiRequest",
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
                (
                    "request_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data zapytania"
                    ),
                ),
                (
                    "monitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="monitor.monitor",
                        verbose_name="Monitor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Odpowiedź API",
                "verbose_name_plural": "Odpowiedźi API",
                "ordering": ["-request_date"],
            },
        ),
    ]
