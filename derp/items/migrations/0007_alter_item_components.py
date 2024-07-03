# Generated by Django 5.0.6 on 2024-07-15 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_components'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='components',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
    ]
