# Generated by Django 4.2.7 on 2023-12-01 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_inscripcione_cedula'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inscripcione',
            new_name='Usuario',
        ),
    ]
