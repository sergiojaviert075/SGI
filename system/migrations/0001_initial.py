# Generated by Django 4.2.5 on 2023-11-04 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('codigo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Código ciudad')),
            ],
            options={
                'verbose_name': 'Canton',
                'verbose_name_plural': 'Cantones',
            },
        ),
        migrations.CreateModel(
            name='CategoriaModulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripción')),
                ('orden', models.IntegerField(default=0, verbose_name='Orden')),
                ('visible', models.BooleanField(default=True, verbose_name='¿Está Visible?')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Categoría de Módulo',
                'verbose_name_plural': 'Categorías de Módulos',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('codigo_pais', models.CharField(blank=True, max_length=200, null=True, verbose_name='Código Pais')),
                ('codigo_telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código télefono')),
                ('codigo_idioma', models.CharField(blank=True, max_length=200, null=True, verbose_name='Código idioma')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('codigo_provincia', models.CharField(blank=True, max_length=200, null=True, verbose_name='Código provincia')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.pais')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('codigo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Código parroquia')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.canton')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Parroquia',
                'verbose_name_plural': 'Parroquias',
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('nombre', models.CharField(default='', max_length=100, unique=True, verbose_name='Nombre')),
                ('icono', models.CharField(blank=True, default='fe fe-clipboard', max_length=100, null=True, verbose_name='Icono')),
                ('url_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='URL name')),
                ('descripcion', models.TextField(blank=True, default='', max_length=300, null=True, verbose_name='Descripción')),
                ('orden', models.IntegerField(default=0, verbose_name='Orden')),
                ('visible', models.BooleanField(default=True, verbose_name='¿Está Visible?')),
                ('es_modulo_padre', models.BooleanField(default=False, verbose_name='¿Es módulo padre?')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.categoriamodulo', verbose_name='Categoría')),
                ('modulo_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.modulo', verbose_name='Módulo Padre')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Módulo',
                'verbose_name_plural': 'Módulos',
            },
        ),
        migrations.AddField(
            model_name='canton',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.provincia'),
        ),
        migrations.AddField(
            model_name='canton',
            name='usuario_creacion',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación'),
        ),
        migrations.AddField(
            model_name='canton',
            name='usuario_modificacion',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación'),
        ),
        migrations.CreateModel(
            name='AccesoModulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('status', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('activo', models.BooleanField(default=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.modulo')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creación')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación')),
            ],
            options={
                'verbose_name': 'Acceso a módulo',
                'verbose_name_plural': 'Acceso a módulos',
                'ordering': ['id'],
            },
        ),
    ]
