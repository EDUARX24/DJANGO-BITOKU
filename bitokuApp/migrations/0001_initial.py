# Generated by Django 5.1.1 on 2024-09-15 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=20, verbose_name='Nombre de Usuario')),
                ('contrasenia', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('rol', models.CharField(max_length=20, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]
