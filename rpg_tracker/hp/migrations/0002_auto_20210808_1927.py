# Generated by Django 3.1.3 on 2021-08-08 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periciasespecializacoes',
            name='pericia_parent',
        ),
        migrations.AddField(
            model_name='periciasespecializacoes',
            name='pericia_pai',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='especializacoes', to='hp.periciasespecializacoes', verbose_name='Perícia pai'),
        ),
    ]