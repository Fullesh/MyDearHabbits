# Generated by Django 5.0.6 on 2024-06-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habbits', '0005_remove_habbit_users_habbit_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habbit',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время когда выполняется привычка'),
        ),
    ]
