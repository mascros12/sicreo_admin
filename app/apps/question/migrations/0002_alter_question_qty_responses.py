# Generated by Django 4.2.3 on 2023-08-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qty_responses',
            field=models.SmallIntegerField(choices=[(2, 'Pregunta de Si/No'), (5, 'Pregunta escala del 1-3')]),
        ),
    ]
