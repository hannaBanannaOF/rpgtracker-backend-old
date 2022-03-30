# Generated by Django 4.0.3 on 2022-03-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureToggle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feature', models.CharField(choices=[('NEW_LOGIN', 'Novo login')], max_length=45, verbose_name='Feature')),
                ('active', models.BooleanField(default=False, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Feature toggle',
                'verbose_name_plural': 'Features toggle',
            },
        ),
    ]
