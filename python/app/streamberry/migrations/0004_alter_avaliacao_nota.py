# Generated by Django 4.1 on 2023-12-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamberry', '0003_alter_avaliacao_usuario_alter_filme_avaliacoes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.FloatField(help_text='Nota de 0 a 5'),
        ),
    ]