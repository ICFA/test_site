# Generated by Django 5.0.4 on 2024-04-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu_Utilization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr_util', models.CharField(max_length=5)),
                ('log_time', models.DateTimeField(verbose_name='log time')),
            ],
        ),
    ]
