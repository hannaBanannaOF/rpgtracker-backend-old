# Generated by Django 3.1.3 on 2021-06-19 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_usuario_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesabase',
            name='fichas',
        ),
        migrations.AddField(
            model_name='mesabase',
            name='open_session',
            field=models.BooleanField(default=False, verbose_name='Sessão aberta'),
        ),
        migrations.CreateModel(
            name='FichaInMesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('in_session', models.BooleanField(default=False, verbose_name='Está online')),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesas', to='core.fichabase', verbose_name='Ficha')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fichas', to='core.mesabase', verbose_name='Mesa')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
