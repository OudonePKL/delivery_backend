# Generated by Django 4.2.4 on 2024-03-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_productimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="color",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderitem",
            name="size",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
