# Generated by Django 3.1.3 on 2020-11-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0012_auto_20201109_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='classednd',
            name='prequesitie_races',
            field=models.ManyToManyField(blank=True, null=True, related_name='racas_prereq', to='dnd.RacesDND', verbose_name='Prerequisitos de raça'),
        ),
    ]