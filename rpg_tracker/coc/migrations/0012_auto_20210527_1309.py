# Generated by Django 3.1.3 on 2021-05-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coc', '0011_auto_20210527_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapons',
            name='rounds_left',
        ),
        migrations.AddField(
            model_name='weaponsinficha',
            name='rounds_left',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tiros restantes'),
        ),
    ]
