# Generated by Django 4.0.4 on 2022-06-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sl_app', '0004_remove_cliente_nombrecliente_cliente_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='name',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombreCliente',
            field=models.CharField(default='Nombre de Cliente', max_length=20),
        ),
    ]
