# Generated by Django 4.1.13 on 2024-11-10 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_rename_bairro_empresa_empresa_bairro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacao',
            name='disponivel_produto',
        ),
    ]
