# Generated by Django 4.1 on 2022-09-02 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Id",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(default="", upload_to="images")),
                ("first_name", models.CharField(max_length=15)),
                ("last_name", models.CharField(max_length=15)),
                ("location", models.CharField(max_length=20)),
                ("sex", models.CharField(max_length=20)),
                ("citizen", models.CharField(max_length=20)),
                ("card_num", models.CharField(max_length=20)),
                ("number_id", models.CharField(max_length=11)),
                ("date_of_birth", models.DateField(default=django.utils.timezone.now)),
                ("validit_period", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
