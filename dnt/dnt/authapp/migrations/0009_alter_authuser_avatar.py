# Generated by Django 4.1.7 on 2023-04-10 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_authuser_current_lp_authuser_division_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users', verbose_name='Аватар'),
        ),
    ]
