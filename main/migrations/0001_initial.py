# Generated by Django 3.0.3 on 2020-04-16 15:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.TextField()),
                ('supplier_location', models.TextField()),
                ('supplier_Phonenumber', models.TextField()),
                ('supplier_email', models.EmailField(max_length=254)),
                ('supplier_website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_description', models.TextField(max_length=100)),
                ('tag_number', models.TextField(unique=True)),
                ('asset_cost', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('monthly_depreciation', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('total_depreciation', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('current_cost', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('serial_number', models.TextField()),
                ('category', models.TextField(choices=[('COMPUTERS', 'COMPUTER'), ('FURNITURES', 'FURNITURE'), ('OFFICE_EQUIPMENT', 'OFFICE EQUIPMENT'), ('LINK_EQUIPMENT', 'LINK EQUIPMENT'), ('SERVERS', 'SERVERS')])),
                ('location', models.TextField(choices=[('BRANCH_1', 'BRANCH 1'), ('BRANCH_2', 'BRANCH 2'), ('BRANCH_3', 'BRANCH 3'), ('BRANCH_4', 'BRANCH 5'), ('BRANCH_5', 'BRANCH 5')])),
                ('date_in_service', models.DateField(default=datetime.date.today)),
                ('status', models.TextField(default='IN USE', max_length=100)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplied_by', to='main.Supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]