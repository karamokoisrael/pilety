# Generated by Django 4.2.3 on 2023-07-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allin', '0004_loosecargo_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loosecargo',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='This is auto generated', max_digits=10, null=True, verbose_name='Total Cost'),
        ),
    ]
