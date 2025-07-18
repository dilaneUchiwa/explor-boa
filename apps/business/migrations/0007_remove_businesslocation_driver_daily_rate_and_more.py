# Generated by Django 5.2.2 on 2025-07-05 19:35

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_businesslocation_driver_daily_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesslocation',
            name='driver_daily_rate',
        ),
        migrations.AddField(
            model_name='business',
            name='commission_rate',
            field=models.DecimalField(decimal_places=2, default=Decimal('5.00'), help_text='Percentage of commission taken by the platform (e.g., 5.00 for 5%)', max_digits=5, verbose_name='Commission Rate (%)'),
        ),
    ]
