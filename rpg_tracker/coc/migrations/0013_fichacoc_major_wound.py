# Generated by Django 3.1.3 on 2021-05-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coc', '0012_auto_20210527_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichacoc',
            name='major_wound',
            field=models.BooleanField(default=False, verbose_name='Major wound'),
        ),
    ]