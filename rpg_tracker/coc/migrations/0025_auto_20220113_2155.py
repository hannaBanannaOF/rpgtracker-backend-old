# Generated by Django 3.1.3 on 2022-01-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coc', '0024_auto_20220113_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_rarity',
            field=models.IntegerField(choices=[(0, 'Comum'), (1, '1920 Era'), (2, 'Moderna'), (3, 'Pulp')], verbose_name='Raridade'),
        ),
    ]