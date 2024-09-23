# Generated by Django 5.1 on 2024-09-02 02:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre_profesion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre_especialidad', models.CharField(max_length=50)),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.profesion')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.especialidad')),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.profesion')),
            ],
        ),
    ]
