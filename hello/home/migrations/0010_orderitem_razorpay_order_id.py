# Generated by Django 3.2.25 on 2024-07-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20240725_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
