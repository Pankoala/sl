# Generated by Django 4.0.4 on 2022-06-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sl_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='name',
            field=models.CharField(default='foobar', max_length=20),
        ),
    ]