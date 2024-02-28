# Generated by Django 4.2.10 on 2024-02-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_monitor_alter_log_options_alter_log_cert_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['request_date'], 'verbose_name': 'Log', 'verbose_name_plural': 'Logi'},
        ),
        migrations.AlterModelOptions(
            name='monitor',
            options={'ordering': ['add_date'], 'verbose_name': 'Monitor', 'verbose_name_plural': 'Monitory'},
        ),
        migrations.AlterField(
            model_name='monitor',
            name='is_active',
            field=models.BooleanField(verbose_name='Czy aktywny?'),
        ),
    ]
