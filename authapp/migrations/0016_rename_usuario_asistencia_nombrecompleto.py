# Generated by Django 4.2.7 on 2024-01-25 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_remove_asistencia_entrenador_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistencia',
            old_name='Usuario',
            new_name='NombreCompleto',
        ),
    ]
