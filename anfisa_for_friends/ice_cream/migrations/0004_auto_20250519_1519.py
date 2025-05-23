# Generated by Django 3.2.16 on 2025-05-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_alter_wrapper_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
