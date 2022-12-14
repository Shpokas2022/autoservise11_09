# Generated by Django 4.1.3 on 2022-11-09 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10, verbose_name='license_number')),
                ('vin', models.CharField(max_length=30, verbose_name='VIN number')),
                ('client', models.CharField(max_length=200, verbose_name='client')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50, verbose_name='make')),
                ('model', models.CharField(max_length=50, verbose_name='model')),
                ('year', models.IntegerField(choices=[(2022, '2022'), (2021, '2021'), (2020, '2020'), (2019, '2019'), (2018, '2018'), (2017, '2017'), (2016, '2016'), (2015, '2015'), (2014, '2014'), (2013, '2013'), (2012, '2012'), (2011, '2011'), (2010, '2010'), (2009, '2009'), (2008, '2008'), (2007, '2007'), (2006, '2006'), (2005, '2005'), (2004, '2004'), (2003, '2003'), (2002, '2002'), (2001, '2001'), (2000, '2000'), (1999, '1999'), (1998, '1998'), (1997, '1997'), (1996, '1996'), (1995, '1995'), (1994, '1994'), (1993, '1993'), (1992, '1992'), (1991, '1991'), (1990, '1990'), (1989, '1989')], verbose_name='year')),
                ('engine', models.CharField(max_length=50, verbose_name='engine')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='total amount')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='automoto.car', verbose_name='car')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='automoto.order', verbose_name='order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='automoto.service', verbose_name='service')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='automoto.carmodel', verbose_name='car_model'),
        ),
    ]
