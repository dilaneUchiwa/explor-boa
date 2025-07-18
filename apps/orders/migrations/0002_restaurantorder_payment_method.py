# Generated by Django 5.2.2 on 2025-07-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantorder',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'Espèces'), ('WALLET', 'Portefeuille'), ('MOBILE_MONEY', 'Mobile Money'), ('CARD', 'Carte bancaire')], default='CASH', help_text='Mode de paiement utilisé pour la commande', max_length=20, verbose_name='Mode de paiement'),
        ),
    ]
