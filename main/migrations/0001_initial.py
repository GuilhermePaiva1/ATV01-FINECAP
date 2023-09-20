# Generated by Django 4.2.5 on 2023-09-19 13:16

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('localizacao', models.CharField(max_length=50, verbose_name='Localização')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET(core.models.get_sentinel_user), related_name='created_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET(core.models.get_sentinel_user), related_name='updated_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Stand',
                'verbose_name_plural': 'Stands',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('cnpj_empresa', models.CharField(max_length=50, null=True, verbose_name='CNPJ Empresa')),
                ('nome_empresa', models.CharField(max_length=255, verbose_name='Nome Empresa')),
                ('email_empresa', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('categoria_empresa', models.CharField(choices=[('TECNOLOGIA', 'Tecnologia'), ('AGRO', 'Agro Negócio')], max_length=50, verbose_name='Categoria Empresa')),
                ('quitado', models.BooleanField(default=False, verbose_name='Quitado')),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET(core.models.get_sentinel_user), related_name='created_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stand', verbose_name='Stand')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET(core.models.get_sentinel_user), related_name='updated_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]