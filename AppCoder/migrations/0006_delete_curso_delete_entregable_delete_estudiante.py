# Generated by Django 4.1.3 on 2022-12-26 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_service'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
