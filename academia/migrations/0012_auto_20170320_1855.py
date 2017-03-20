# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0011_auto_20170317_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dobra',
            name='metodo',
            field=models.CharField(choices=[('durnin_womersley_1974', 'Durnin Womersley 1974'), ('pestroski_1995_mulher', 'Pestroski 1995 (mulheres, 18 a 61 anos)'), ('jackson_pollock_1978', 'Jackson, Pollock 1984'), ('pollock_schimidt_jackson_1980', 'Pollock, Schimidt e Jackson 1980 (adultos)'), ('pestroski_1995_homem', 'Pestroski 1995 (homens, 18 a 61 anos)'), ('jackson_pollock_ward_1980', 'Jackson, Pollock e Ward 1980 (mulheres, 18 a 55 anos)'), ('jackson_pollock_ward_1984', 'Jackson, Pollock e Ward 1984')], max_length=50),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='abdome',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='altura',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='antebracodireito',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='antebracoesquerdo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='bicipesdireito',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='bicipesesquedo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='cintura',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='coxadireita',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='coxaesquerda',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='panturrilhadireta',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='panturrilhaesquerda',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='pescoco',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='peso',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='quadril',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='torax',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='tricipesdireito',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='perimetria',
            name='tricipesesquerdo',
            field=models.FloatField(null=True),
        ),
    ]
