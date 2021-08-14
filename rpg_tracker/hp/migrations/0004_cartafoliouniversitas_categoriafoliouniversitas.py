# Generated by Django 3.1.3 on 2021-08-14 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0003_equipamentoficha_equipamentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaFolioUniversitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('imgBase64', models.TextField(verbose_name='Imagem (Base64)')),
            ],
            options={
                'verbose_name': 'categoria Folio Universitas',
                'verbose_name_plural': 'categorias Folio Universitas',
            },
        ),
        migrations.CreateModel(
            name='CartaFolioUniversitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('imgBase64', models.TextField(verbose_name='Imagem (Base64)')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('anoNasc', models.IntegerField(blank=True, null=True, verbose_name='Nascimento')),
                ('anoMort', models.IntegerField(blank=True, null=True, verbose_name='Nascimento')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartas', to='hp.categoriafoliouniversitas', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'carta Folio Universitas',
                'verbose_name_plural': 'cartas Folio Universitas',
            },
        ),
    ]
