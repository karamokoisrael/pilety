# Generated by Django 4.2.3 on 2023-07-07 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_supplied', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='loosecargo',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cargos', to='allin.delivery'),
        ),
        migrations.AddField(
            model_name='loosecargo',
            name='dispature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loose_cargos_dispatched', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='loosecargo',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loose_cargos_recieved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='cargo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='allin.loosecargo'),
        ),
        migrations.AddField(
            model_name='fullcargo',
            name='dispature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='full_cargos_dispatched', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='dispature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='allin.expensecategory', verbose_name='Name of the expense'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delivery',
            name='vehicle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='allin.deliveryvehicle'),
        ),
        migrations.AddField(
            model_name='loosecargo',
            name='container',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cargos', to='allin.loosecontainer'),
        ),
        migrations.AddField(
            model_name='fullcontainer',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fullcontainers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fullcargo',
            name='container',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cargos', to='allin.fullcontainer'),
        ),
    ]
