# Generated by Django 5.0.6 on 2024-06-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='ID в телеграмм'),
        ),
    ]
