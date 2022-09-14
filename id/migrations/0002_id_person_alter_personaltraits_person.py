# Generated by Django 4.1.1 on 2022-09-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("id", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="id",
            name="person",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="pers", to="id.personaltraits"
            ),
        ),
        migrations.AlterField(
            model_name="personaltraits",
            name="person",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
