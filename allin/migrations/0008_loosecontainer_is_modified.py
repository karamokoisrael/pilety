# Generated by Django 4.2.3 on 2023-09-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allin', '0007_alter_product_prod_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='loosecontainer',
            name='is_modified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
