# Generated by Django 4.1.3 on 2022-11-24 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_autor_options_libro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
    ]