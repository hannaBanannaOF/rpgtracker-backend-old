# Generated by Django 3.1.3 on 2020-11-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0003_auto_20201103_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='character_level',
            field=models.IntegerField(default=1, verbose_name='Nível de personagem'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='proficiency_bonus',
            field=models.IntegerField(default=2, verbose_name='Bônus de proficiência'),
        ),
    ]
