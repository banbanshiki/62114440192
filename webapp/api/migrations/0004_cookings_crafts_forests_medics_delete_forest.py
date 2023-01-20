# Generated by Django 4.1.3 on 2022-12-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_delete_eqipment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cookings",
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
                ("Menu", models.TextField(verbose_name="เมนู")),
                ("Rawmaterial", models.TextField(verbose_name="วัตถุดิบ")),
                ("Method", models.TextField(verbose_name="วิธีทำ")),
            ],
        ),
        migrations.CreateModel(
            name="Crafts",
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
                ("Menu", models.TextField(verbose_name="เมนู")),
                ("Method", models.TextField(verbose_name="วิธีทำ")),
            ],
        ),
        migrations.CreateModel(
            name="Forests",
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
                ("name", models.TextField(verbose_name="ชื่อ")),
                ("image", models.ImageField(upload_to="images", verbose_name="รูป")),
                ("Level", models.TextField(verbose_name="ความยาก")),
                ("Season", models.TextField(verbose_name="เดือน/ฤดูกาล")),
                ("Distance", models.TextField(verbose_name="ระยะทาง")),
                ("Time", models.TextField(verbose_name="เวลา")),
                ("Details", models.TextField(verbose_name="รายละเอียด")),
            ],
        ),
        migrations.CreateModel(
            name="Medics",
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
                ("Symptom", models.TextField(verbose_name="อาการ")),
                ("Remedy", models.TextField(verbose_name="วิธีรักษา")),
            ],
        ),
        migrations.DeleteModel(
            name="Forest",
        ),
    ]