# Generated by Django 4.2.1 on 2024-05-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="original_bag",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="order",
            name="stripe_pid",
            field=models.CharField(default="", max_length=254),
        ),
        migrations.AlterField(
            model_name="order",
            name="grand_total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
