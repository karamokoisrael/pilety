# Generated by Django 4.1.7 on 2023-04-04 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_consignee_options_and_more'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('bank_url', models.URLField(blank=True, null=True, verbose_name=' Internet banking link')),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='users.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True, verbose_name='Product or Service')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('ammount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('from_ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_to', to='finance.account')),
                ('to_ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recieved_from', to='finance.account')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('has_tax', models.BooleanField(blank=True, default=True, null=True)),
                ('is_recurring', models.BooleanField(blank=True, default=False, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('invoice_no', models.CharField(blank=True, max_length=10, null=True, verbose_name='Invoice number')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Invoice date')),
                ('sales_tax', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='users.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='finance.product', verbose_name='Product/Service')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/documents/expenses')),
                ('ammount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='finance.account')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/documents/deposits')),
                ('ammount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposits', to='finance.account')),
            ],
        ),
    ]