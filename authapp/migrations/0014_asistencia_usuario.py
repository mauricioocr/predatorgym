# Generated by Django 4.2.7 on 2024-01-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_asistencia_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='Usuario',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
