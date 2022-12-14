# Generated by Django 4.1.3 on 2022-11-24 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autore', 'verbose_name_plural': 'Autores'},
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('fecha_publicada', models.DateField(verbose_name='Fecha publicada')),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='libro.autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
