# Generated by Django 4.2.10 on 2024-02-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0017_alter_log_status_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='ssl_monitor',
            field=models.BooleanField(null=True, verbose_name='Monitorować SSL?'),
        ),
    ]
