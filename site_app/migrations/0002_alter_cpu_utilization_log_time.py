# Generated by Django 5.0.4 on 2024-04-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu_utilization',
            name='log_time',
            field=models.DateTimeField(default='15:28:00', editable=False),
        ),
    ]
