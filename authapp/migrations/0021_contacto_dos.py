# Generated by Django 4.2.7 on 2024-05-24 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0020_alter_asistencia_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_dos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Apellido', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Descripcion', models.TextField()),
            ],
        ),
    ]
