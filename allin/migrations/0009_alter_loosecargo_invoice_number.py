# Generated by Django 4.2.3 on 2023-09-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allin', '0008_loosecontainer_is_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loosecargo',
            name='invoice_number',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
