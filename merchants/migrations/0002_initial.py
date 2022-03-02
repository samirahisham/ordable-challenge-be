# Generated by Django 4.0.2 on 2022-02-26 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchants', '0001_initial'),
        ('user', '0002_storemerchant_storedriver'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.storedriver'),
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.item'),
        ),
    ]
