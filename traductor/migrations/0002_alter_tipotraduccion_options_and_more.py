# Generated by Django 4.1.6 on 2023-11-24 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traductor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipotraduccion',
            options={'verbose_name': 'TipoTraduccion', 'verbose_name_plural': 'TiposTraducciones'},
        ),
        migrations.AlterModelOptions(
            name='traduccion',
            options={'verbose_name': 'Traduccion', 'verbose_name_plural': 'Traducciones'},
        ),
    ]