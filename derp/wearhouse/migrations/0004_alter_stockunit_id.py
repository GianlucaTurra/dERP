# Generated by Django 5.0.6 on 2024-08-29 22:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wearhouse', '0003_alter_stockunit_options_stockunit_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockunit',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]