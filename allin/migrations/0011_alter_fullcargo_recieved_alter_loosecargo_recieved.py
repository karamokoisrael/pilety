# Generated by Django 4.2.3 on 2023-09-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allin', '0010_product_cost_per_cbm_alter_product_packaging_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullcargo',
            name='recieved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loosecargo',
            name='recieved',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
