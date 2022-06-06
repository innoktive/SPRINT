# Generated by Django 4.0.5 on 2022-06-05 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_asignatura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignatura',
            old_name='nombre',
            new_name='apellido',
        ),
        migrations.AlterField(
            model_name='profesor',
            name='fecha_contratacion',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 5)),
        ),
    ]
