# Generated by Django 5.2.2 on 2025-07-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_add_user_action_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesslocation',
            name='driver_daily_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Tarif chauffeur par jour (FCFA)'),
        ),
    ]
