# Generated by Django 5.1 on 2024-08-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_noticia_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="bodega",
            name="descripcion",
            field=models.TextField(default="Sin descripción"),
        ),
        migrations.AddField(
            model_name="bodega",
            name="disponible",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="tipobodega",
            name="tipo",
            field=models.CharField(max_length=100),
        ),
    ]
