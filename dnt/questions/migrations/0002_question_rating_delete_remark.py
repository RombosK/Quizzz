# Generated by Django 4.1.7 on 2023-03-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="rating",
            field=models.IntegerField(default=0, verbose_name="Очки"),
        ),
        migrations.DeleteModel(name="Remark",),
    ]