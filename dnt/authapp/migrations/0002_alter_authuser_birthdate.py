# Generated by Django 4.1.7 on 2023-03-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authuser",
            name="birthdate",
            field=models.DateField(null=True, verbose_name="Дата рождения"),
        ),
    ]