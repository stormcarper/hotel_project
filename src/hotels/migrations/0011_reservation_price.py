# Generated by Django 4.2.19 on 2025-03-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0010_reservation"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="price",
            field=models.CharField(default="default_price", max_length=20),
        ),
    ]
