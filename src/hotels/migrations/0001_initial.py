# Generated by Django 4.2.19 on 2025-02-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotels",
            fields=[
                ("hotel_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=30)),
            ],
        ),
    ]
