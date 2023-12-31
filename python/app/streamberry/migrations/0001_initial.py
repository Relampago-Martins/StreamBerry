# Generated by Django 4.1 on 2023-12-31 02:49

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
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(help_text='Nota de 0 a 5')),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Streaming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('mes', models.IntegerField(choices=[(1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')])),
                ('ano', models.IntegerField()),
                ('genero', models.CharField(max_length=255)),
                ('avaliacoes', models.ManyToManyField(through='streamberry.Avaliacao', to=settings.AUTH_USER_MODEL)),
                ('streamings', models.ManyToManyField(to='streamberry.streaming')),
            ],
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='filme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streamberry.filme'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
