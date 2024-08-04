# Generated by Django 5.0.6 on 2024-08-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_remove_item_depth_mm_remove_item_height_mm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='volume_cm3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='weigth_g',
        ),
        migrations.AddField(
            model_name='item',
            name='volume',
            field=models.FloatField(default=0.0, verbose_name='Volume'),
        ),
        migrations.AddField(
            model_name='item',
            name='volume_measure',
            field=models.CharField(choices=[('mm3', 'Cubic millimetre'), ('cm3', 'Cubic centimetre')], default='cm3', max_length=5, verbose_name='Volume measure unit'),
        ),
        migrations.AddField(
            model_name='item',
            name='weigth',
            field=models.FloatField(default=0.0, verbose_name='Weigth'),
        ),
        migrations.AddField(
            model_name='item',
            name='weigth_measure',
            field=models.CharField(choices=[('g', 'Grams'), ('hg', 'Hectograms'), ('kg', 'Kilograms')], default='g', max_length=10, verbose_name='Weigth measure unit'),
        ),
    ]