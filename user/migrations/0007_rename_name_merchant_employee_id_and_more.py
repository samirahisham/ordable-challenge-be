# Generated by Django 4.0.2 on 2022-03-02 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_merchant_merchant_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchant',
            old_name='name',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='storedriver',
            old_name='name',
            new_name='employee_id',
        ),
    ]