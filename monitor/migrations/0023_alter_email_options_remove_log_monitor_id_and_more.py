# Generated by Django 5.0.2 on 2024-03-06 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0022_alter_statuspage_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ['email'], 'verbose_name': 'Adres e-mail', 'verbose_name_plural': 'Emaile'},
        ),
        migrations.RemoveField(
            model_name='log',
            name='monitor_id',
        ),
        migrations.AddField(
            model_name='log',
            name='monitor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='monitor.monitor', verbose_name='Monitor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monitor',
            name='monitor_type',
            field=models.CharField(choices=[('http_request', 'Zapytanie HTTP'), ('ping', 'Ping'), ('cron job', 'Crone Job')], default='http_request', max_length=15, verbose_name='Typ monitorowania'),
        ),
    ]
