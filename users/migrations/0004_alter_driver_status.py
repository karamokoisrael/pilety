# Generated by Django 4.1.7 on 2023-04-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_consignee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'ACTIVE'), ('TERMINATED', 'TERMINATED'), ('TEMPORARY', 'TEMPORARY')], default='ACTIVE', max_length=10, null=True),
        ),
    ]
