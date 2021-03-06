# Generated by Django 4.0.2 on 2022-03-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0007_alter_order_destination_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination_lat',
            field=models.DecimalField(decimal_places=16, max_digits=18),
        ),
        migrations.AlterField(
            model_name='order',
            name='destination_long',
            field=models.DecimalField(decimal_places=16, max_digits=18),
        ),
    ]
