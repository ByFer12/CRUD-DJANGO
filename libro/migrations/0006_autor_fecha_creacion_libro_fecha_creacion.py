# Generated by Django 4.1.3 on 2022-11-24 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_remove_libro_autor_libro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='Fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
    ]
