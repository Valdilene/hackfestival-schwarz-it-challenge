# Generated by Django 5.1.1 on 2024-09-07 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_item_expiresat_alter_item_weight'),
        ('upCycleRequest', '0005_alter_upcyclerequest_requestsat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='upCycleRequest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='upCycleRequest.upcyclerequest'),
        ),
    ]
