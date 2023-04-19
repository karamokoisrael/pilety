# Generated by Django 4.1.7 on 2023-04-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0007_fullcontainer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullcargo',
            name='cargo_cbm',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=10, null=True, verbose_name='Cargo CBM'),
        ),
        migrations.AddField(
            model_name='loosecargo',
            name='cargo_cbm',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=10, null=True, verbose_name='Cargo CBM'),
        ),
    ]