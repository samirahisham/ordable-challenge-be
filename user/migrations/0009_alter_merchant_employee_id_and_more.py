# Generated by Django 4.0.2 on 2022-03-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_storemerchant_merchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='employee_id',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='storedriver',
            name='employee_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
