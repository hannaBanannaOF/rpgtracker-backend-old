# Generated by Django 3.1.3 on 2021-08-08 19:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_auto_20210621_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriaturaMagica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Criatura')),
                ('classificacao_MM', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Classificação Ministério da Magia')),
            ],
            options={
                'verbose_name': 'criatura mágica',
                'verbose_name_plural': 'criaturas mágicas',
            },
        ),
        migrations.CreateModel(
            name='FichaHP',
            fields=[
                ('fichabase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.fichabase')),
                ('escola', models.CharField(blank=True, max_length=255, null=True, verbose_name='Escola')),
                ('ano_escolar', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)], verbose_name='Ano Escolar')),
                ('casa_hogwarts', models.IntegerField(blank=True, choices=[(0, 'Grifinória'), (1, 'Sonserina'), (2, 'Corvinal'), (3, 'Lufa-lufa')], null=True, verbose_name='Casa de Hogwarts')),
                ('familiar', models.CharField(blank=True, max_length=255, null=True, verbose_name='Familiar (nome & tipo)')),
                ('atletismo', models.IntegerField(default=0, verbose_name='Atletismo')),
                ('conhecimento', models.IntegerField(default=0, verbose_name='Conhecimento')),
                ('intriga', models.IntegerField(default=0, verbose_name='Intriga')),
                ('magia', models.IntegerField(default=0, verbose_name='Magia')),
            ],
            options={
                'verbose_name': 'ficha',
                'verbose_name_plural': 'fichas',
            },
            bases=('core.fichabase',),
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('mesabase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.mesabase')),
            ],
            options={
                'verbose_name': 'mesa',
                'verbose_name_plural': 'mesas',
            },
            bases=('core.mesabase',),
        ),
        migrations.CreateModel(
            name='PericiasEspecializacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('aptidao', models.IntegerField(blank=True, choices=[(0, 'Atletismo'), (1, 'Intriga'), (2, 'Conhecimento'), (3, 'Magia')], null=True, verbose_name='Aptidão')),
                ('pericia_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pericia_pai', to='hp.periciasespecializacoes', verbose_name='Perícia pai')),
            ],
            options={
                'verbose_name': 'perícia e aptidão',
                'verbose_name_plural': 'perícias e aptidões',
            },
        ),
        migrations.CreateModel(
            name='Varinha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nucleo', models.IntegerField(choices=[(0, 'Pena da cauda de fênix'), (1, 'Corda de coração de dragão'), (2, 'Pelo de unicórnio'), (3, 'Cabelo de veela'), (4, 'Chifre de serpente chifruda dos rios')], verbose_name='Núcleo')),
                ('madeira', models.IntegerField(choices=[(0, 'Bétula'), (1, 'Sovieira'), (2, 'Freixo'), (3, 'Amieiro'), (4, 'Sabugueiro'), (5, 'Abrunheiro'), (6, 'Carvalho'), (7, 'Azevinho'), (8, 'Avelã'), (9, 'Videira'), (10, 'Hedera'), (11, 'Sequoia')], verbose_name='Madeira')),
                ('tamanho', models.FloatField(verbose_name='Tamanho')),
                ('flexibilidade', models.IntegerField(choices=[(0, 'Dobrável'), (1, 'Surpreendentemente suave'), (2, 'Suave'), (3, 'Ligeiramente suave'), (4, 'Bastante curvada'), (5, 'Muito flexível'), (6, 'Bastante flexível'), (7, 'Flexível'), (8, 'Razoavelmente flexível'), (9, 'Maleável'), (10, 'Frágil'), (11, 'Áspera'), (12, 'Maciça'), (13, 'Viscosa'), (14, 'Rígida'), (15, 'Inflexível'), (16, 'Levemente inflexível'), (17, 'Resoluta'), (18, 'Macia')], verbose_name='Flexibilidade')),
            ],
            options={
                'verbose_name': 'varinha',
                'verbose_name_plural': 'varinhas',
            },
        ),
        migrations.CreateModel(
            name='PericiasEspecializacoesFicha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('valor', models.IntegerField(verbose_name='Valor')),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='pericias', to='hp.fichahp', verbose_name='Ficha')),
                ('pericia', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='fichas', to='hp.periciasespecializacoes', verbose_name='Perícias e especializações')),
            ],
            options={
                'verbose_name': 'perícia/especialização em ficha',
                'verbose_name_plural': 'perícias/especializações em fichas',
            },
        ),
        migrations.AddField(
            model_name='fichahp',
            name='varinha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='bruxo', to='hp.varinha', verbose_name='Varinha'),
        ),
        migrations.CreateModel(
            name='EspecializacoesCustomizadasPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('valor', models.IntegerField(verbose_name='Valor')),
                ('hint', models.CharField(max_length=255, verbose_name='Dica')),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='especializacoes_custom', to='hp.fichahp', verbose_name='Ficha')),
                ('pericia_pai', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='especializacoes_custom', to='hp.periciasespecializacoes', verbose_name='Perícia pai')),
            ],
            options={
                'verbose_name': 'especialização customizada por player',
                'verbose_name_plural': 'especializações customizadas por player',
            },
        ),
    ]
