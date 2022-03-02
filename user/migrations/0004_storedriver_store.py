# Generated by Django 4.0.2 on 2022-02-26 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0002_initial'),
        ('user', '0003_storedriver_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedriver',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='merchants.store'),
            preserve_default=False,
        ),
    ]
