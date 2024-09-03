# Generated by Django 5.0.6 on 2024-08-29 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wearhouse', '0004_alter_stockunit_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockunit',
            name='cacca',
            field=models.FloatField(null=True, verbose_name='cacca'),
        ),
        migrations.AlterField(
            model_name='stockunit',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Stock unit name'),
        ),
    ]
