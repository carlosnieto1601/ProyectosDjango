# Generated by Django 4.0.4 on 2022-05-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='correo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='numero',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
