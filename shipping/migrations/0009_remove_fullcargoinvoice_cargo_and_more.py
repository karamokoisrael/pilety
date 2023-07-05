# Generated by Django 4.2.2 on 2023-07-05 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0008_fullcargo_cargo_cbm_loosecargo_cargo_cbm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fullcargoinvoice',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='fullcontainer',
            name='dispatcher',
        ),
        migrations.RemoveField(
            model_name='loosecargo',
            name='checked_by',
        ),
        migrations.RemoveField(
            model_name='loosecargo',
            name='loose_container',
        ),
        migrations.RemoveField(
            model_name='loosecargo',
            name='product',
        ),
        migrations.RemoveField(
            model_name='loosecargo',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='loosecargoinvoice',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='loosecontainer',
            name='dispatcher',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='consignee',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='shipper',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='driver',
        ),
        migrations.DeleteModel(
            name='FullCargo',
        ),
        migrations.DeleteModel(
            name='FullCargoInvoice',
        ),
        migrations.DeleteModel(
            name='FullContainer',
        ),
        migrations.DeleteModel(
            name='LooseCargo',
        ),
        migrations.DeleteModel(
            name='LooseCargoInvoice',
        ),
        migrations.DeleteModel(
            name='LooseContainer',
        ),
        migrations.DeleteModel(
            name='Shipment',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
