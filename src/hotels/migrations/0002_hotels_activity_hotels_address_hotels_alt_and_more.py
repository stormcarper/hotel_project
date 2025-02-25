# Generated by Django 4.2.19 on 2025-02-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotels",
            name="activity",
            field=models.CharField(default="default_activity", max_length=100),
        ),
        migrations.AddField(
            model_name="hotels",
            name="address",
            field=models.CharField(default="default_address", max_length=100),
        ),
        migrations.AddField(
            model_name="hotels",
            name="alt",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="availability",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="hotels",
            name="checkin",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="checkout",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="directions",
            field=models.CharField(default="default_directions", max_length=200),
        ),
        migrations.AddField(
            model_name="hotels",
            name="fax",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="hours",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="image",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="price",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="tollfree",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="hotels",
            name="type",
            field=models.CharField(default="default", max_length=20),
        ),
        migrations.AddField(
            model_name="hotels",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="hotels",
            name="name",
            field=models.CharField(default="default_name", max_length=30),
        ),
        migrations.AlterField(
            model_name="hotels",
            name="title",
            field=models.CharField(default="default_title", max_length=50),
        ),
    ]
