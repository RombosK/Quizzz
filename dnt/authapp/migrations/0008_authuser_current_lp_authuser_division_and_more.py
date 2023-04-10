# Generated by Django 4.1.7 on 2023-03-24 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_alter_remark_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='current_lp',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Текущие ранговые очки'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='division',
            field=models.PositiveSmallIntegerField(default=4, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)], verbose_name='Дивизион'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='is_lobby_leader',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='authuser',
            name='rank',
            field=models.CharField(choices=[('iron', 'Железо'), ('bronze', 'Бронза'), ('silver', 'Серебро'), ('gold', 'Золото'), ('platinum', 'Платина'), ('diamond', 'Алмаз'), ('master', 'Мастер'), ('grandmaster', 'Грандмастер'), ('challenger', 'Претендент')], default=('iron', 'Железо'), max_length=16, verbose_name='Ранг'),
        ),
    ]