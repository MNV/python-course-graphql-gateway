from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("geo", "0002_alter_city_region"),
    ]

    operations = [
        migrations.CreateModel(
            name="Weather",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Время изменения"),
                ),
                ("temp", models.FloatField(verbose_name="Температура")),
                ("pressure", models.IntegerField(verbose_name="Давление")),
                ("humidity", models.IntegerField(verbose_name="Влажность")),
                ("wind_speed", models.FloatField(verbose_name="Скорость ветра")),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="Описание"),
                ),
                ("visibility", models.IntegerField(verbose_name="Видимость")),
                ("dt", models.DateTimeField(verbose_name="Время")),
                ("timezone", models.IntegerField(verbose_name="Временная зона")),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="city",
                        to="geo.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Погода",
                "verbose_name_plural": "Погода",
            },
        )
    ]