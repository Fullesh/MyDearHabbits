# Generated by Django 5.0.6 on 2024-06-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habbits', '0006_alter_habbit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habbit',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время когда выполняется привычка'),
        ),
    ]
