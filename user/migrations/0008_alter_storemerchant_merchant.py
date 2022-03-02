# Generated by Django 4.0.2 on 2022-03-02 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_name_merchant_employee_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storemerchant',
            name='merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_merchant', to='user.merchant'),
        ),
    ]