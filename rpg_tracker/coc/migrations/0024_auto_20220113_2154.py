# Generated by Django 3.1.3 on 2022-01-13 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coc', '0023_auto_20210808_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='PulpTalents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('desc', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Talento (PCoC)',
                'verbose_name_plural': 'Talentos (PCoC)',
            },
        ),
        migrations.AddField(
            model_name='fichacoc',
            name='pulp_archetype',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Arquétipo de Heroi'),
        ),
        migrations.AddField(
            model_name='fichacoc',
            name='pulp_cthulhu',
            field=models.BooleanField(default=False, verbose_name='Pulp Cthulhu'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='appearence',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Aparência'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='constitution',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Constituição'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='dexterity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Destreza'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='education',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Educação'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='inteligence',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Inteligência'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='language_own',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Idioma natural'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='power',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Poder'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='size',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tamanho'),
        ),
        migrations.AlterField(
            model_name='fichacoc',
            name='strength',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Força'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='base_value',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor base'),
        ),
        migrations.AddField(
            model_name='fichacoc',
            name='pulp_talents',
            field=models.ManyToManyField(related_name='fichas', to='coc.PulpTalents', verbose_name='Talentos (PCoC)'),
        ),
    ]