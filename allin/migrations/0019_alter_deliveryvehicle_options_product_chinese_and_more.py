# Generated by Django 4.2.2 on 2023-06-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allin', '0018_alter_delivery_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliveryvehicle',
            options={'verbose_name_plural': 'Delivery Vehicles'},
        ),
        migrations.AddField(
            model_name='product',
            name='chinese',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='chinese desc'),
        ),
        migrations.AddField(
            model_name='product',
            name='ttprice',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='T.T.Price'),
        ),
        migrations.AddField(
            model_name='product',
            name='units',
            field=models.CharField(blank=True, choices=[('PCS', 'Pieces'), ('RLS', 'Rolls'), ('DZN', 'Dozens'), ('BGS', 'Bags')], default='PCS', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='wght',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True, verbose_name='weight/ctn'),
        ),
        migrations.AlterField(
            model_name='basecontainer',
            name='status',
            field=models.CharField(choices=[('RW', 'Recieved in China Warehouse'), ('DC', 'Departed China '), ('AT', 'Arrived in Tanzania'), ('RC', 'Recieved by Customer')], default='RW', max_length=3),
        ),
        migrations.AlterField(
            model_name='fullcargo',
            name='status',
            field=models.CharField(choices=[('RW', 'Recieved in China Warehouse'), ('DC', 'Departed China '), ('AT', 'Arrived in Tanzania'), ('RC', 'Recieved by Customer')], default='RW', max_length=3),
        ),
        migrations.AlterField(
            model_name='loosecargo',
            name='status',
            field=models.CharField(choices=[('RW', 'Recieved in China Warehouse'), ('DC', 'Departed China '), ('AT', 'Arrived in Tanzania'), ('RC', 'Recieved by Customer')], default='RW', max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='cbm',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='CBM/ctns'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cbms',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Total CBM'),
        ),
        migrations.AlterField(
            model_name='product',
            name='packaging',
            field=models.IntegerField(blank=True, null=True, verbose_name='units/ctn'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Unit Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(blank=True, null=True, verbose_name='qty in a ctn'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='total weight'),
        ),
    ]