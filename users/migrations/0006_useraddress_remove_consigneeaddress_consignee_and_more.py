# Generated by Django 4.2.2 on 2023-07-05 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allin', '0029_alter_delivery_driver_alter_expense_dispature_and_more'),
        ('finance', '0010_remove_deposit_account_remove_expenses_account_and_more'),
        ('shipping', '0009_remove_fullcargoinvoice_cargo_and_more'),
        ('users', '0005_supplier_supplieraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': "User's Address",
                'verbose_name_plural': "User's Addresses",
            },
        ),
        migrations.RemoveField(
            model_name='consigneeaddress',
            name='consignee',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='dispatcheraddress',
            name='dispatcher',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='driveraddress',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='shipper',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='shipperaddress',
            name='shipper',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='supplieraddress',
            name='supplier',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, help_text='If you are a supplier upload your business card here', null=True, upload_to='media/users', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, help_text='Write a unique username', max_length=90, null=True, unique=True, verbose_name='User name'),
        ),
        migrations.DeleteModel(
            name='Consignee',
        ),
        migrations.DeleteModel(
            name='ConsigneeAddress',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='CustomerAddress',
        ),
        migrations.DeleteModel(
            name='Dispatcher',
        ),
        migrations.DeleteModel(
            name='DispatcherAddress',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='DriverAddress',
        ),
        migrations.DeleteModel(
            name='Shipper',
        ),
        migrations.DeleteModel(
            name='shipperAddress',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='SupplierAddress',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]
