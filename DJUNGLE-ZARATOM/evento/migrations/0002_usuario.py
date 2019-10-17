# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('', 'G\xeanero'), ('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')], max_length=200)),
                ('idade', models.PositiveIntegerField()),
                ('telefone', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('', 'UF'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('PR', 'Paran\xe1'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'S\xe3o Paulo'), ('TO', 'Tocantins')], max_length=200)),
            ],
        ),
    ]
