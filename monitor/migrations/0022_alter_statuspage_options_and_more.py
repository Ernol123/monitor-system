# Generated by Django 5.0.2 on 2024-03-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0021_statuspage_monitors"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="statuspage",
            options={
                "ordering": ["-name"],
                "verbose_name": "Status strony",
                "verbose_name_plural": "Statusy stron",
            },
        ),
        migrations.AlterField(
            model_name="monitor",
            name="request_timeout",
            field=models.FloatField(verbose_name="Czas oczekiwania na żądanie"),
        ),
    ]
