# Generated by Django 4.2.10 on 2024-03-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0019_alter_monitor_ssl_monitor"),
    ]

    operations = [
        migrations.AddField(
            model_name="log",
            name="days_to_ssl_exp",
            field=models.IntegerField(null=True, verbose_name="Dni do wygaśnięcia certyfikatu ssl"),
        ),
        migrations.AddField(
            model_name="monitor",
            name="days_before_exp",
            field=models.IntegerField(null=True, verbose_name="Ile dni przed poinformować?"),
        ),
        migrations.AlterField(
            model_name="log",
            name="status",
            field=models.CharField(max_length=50, null=True, verbose_name="Status"),
        ),
    ]
