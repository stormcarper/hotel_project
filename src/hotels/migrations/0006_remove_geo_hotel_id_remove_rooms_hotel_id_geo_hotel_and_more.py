# Generated by Django 4.2.19 on 2025-02-25 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0005_rooms_geo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="geo",
            name="hotel_id",
        ),
        migrations.RemoveField(
            model_name="rooms",
            name="hotel_id",
        ),
        migrations.AddField(
            model_name="geo",
            name="hotel",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="geo",
                to="hotels.hotels",
            ),
        ),
        migrations.AddField(
            model_name="rooms",
            name="hotel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rooms",
                to="hotels.hotels",
            ),
        ),
        migrations.AlterField(
            model_name="geo",
            name="lat",
            field=models.CharField(default="default_lat", max_length=20),
        ),
        migrations.AlterField(
            model_name="geo",
            name="lon",
            field=models.CharField(default="default_lon", max_length=20),
        ),
        migrations.AlterField(
            model_name="hotels",
            name="image",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="price",
            field=models.CharField(default="default_price", max_length=20),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="room_type",
            field=models.CharField(default="default_type", max_length=50),
        ),
    ]
