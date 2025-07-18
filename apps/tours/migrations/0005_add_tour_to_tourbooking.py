# Generated by Django 5.2.2 on 2025-07-05 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_tourbooking_amount_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourbooking',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='tours.tour', verbose_name='Tour'),
        ),
    ]
