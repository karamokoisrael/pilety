# Generated by Django 4.1.7 on 2023-04-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='load_type',
            field=models.CharField(blank=True, choices=[('TL', 'TL'), ('LTL', 'LTL')], default='LTL', max_length=3, null=True),
        ),
    ]