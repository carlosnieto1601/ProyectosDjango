# Generated by Django 4.0.4 on 2022-05-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_clases_profesor_alter_estudiantes_apellido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('salon', models.CharField(max_length=100, verbose_name='Salon')),
                ('horario', models.CharField(max_length=100, verbose_name='Horario')),
            ],
        ),
    ]
