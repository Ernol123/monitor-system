# Generated by Django 4.2.10 on 2024-02-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0004_statuspage_delete_test"),
    ]

    operations = [
        migrations.AlterField(
            model_name="log",
            name="cert_from",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="log",
            name="cert_to",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="log",
            name="domain_exp",
            field=models.DateTimeField(null=True),
        ),
    ]
