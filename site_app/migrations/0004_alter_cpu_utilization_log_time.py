# Generated by Django 5.0.4 on 2024-04-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0003_alter_cpu_utilization_log_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu_utilization',
            name='log_time',
            field=models.CharField(default='30 April 16', editable=False, max_length=8),
        ),
    ]