# Generated by Django 5.0.6 on 2024-06-06 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habbits', '0003_habbit_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habbit',
            old_name='is_plesant',
            new_name='is_pleasant',
        ),
        migrations.RenameField(
            model_name='habbit',
            old_name='releated_habbit',
            new_name='related_habbit',
        ),
        migrations.RenameField(
            model_name='habbit',
            old_name='revard',
            new_name='reward',
        ),
    ]