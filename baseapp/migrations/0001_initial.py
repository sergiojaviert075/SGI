# Generated by Django 4.2.5 on 2023-11-04 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombre', models.CharField(max_length=100, verbose_name='Género')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombres', models.CharField(blank=True, max_length=700, null=True, verbose_name='Nombres')),
                ('apellido1', models.CharField(blank=True, max_length=700, null=True, verbose_name='Primer apellido')),
                ('apellido2', models.CharField(blank=True, max_length=700, null=True, verbose_name='Segundo apellido')),
                ('nombres_compleo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Nombres completos')),
                ('cedula', models.CharField(blank=True, db_index=True, max_length=20, null=True, verbose_name='Cédula')),
                ('pasaporte', models.CharField(blank=True, db_index=True, default='', max_length=20, null=True, verbose_name='Pasaporte')),
                ('ruc', models.CharField(blank=True, db_index=True, default='', max_length=20, null=True, verbose_name='Ruc')),
                ('direccion', models.CharField(blank=True, db_index=True, default='', max_length=1000, null=True, verbose_name='Dirección')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha nacimiento')),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono')),
                ('foto', models.FileField(blank=True, null=True, upload_to='fotopersona/', verbose_name='Foto de la persona')),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseapp.genero', verbose_name='Género')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
