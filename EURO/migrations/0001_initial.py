# Generated by Django 3.1 on 2020-08-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EURODaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='dailyData')),
                ('value', models.CharField(max_length=50, verbose_name='dailyValue')),
                ('changeRate', models.CharField(max_length=50, verbose_name='dailyChangeRate')),
                ('changeType', models.CharField(max_length=50, verbose_name='dailyChangeType')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EUROHourly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='hourlyData')),
                ('value', models.CharField(max_length=50, verbose_name='hourlyValue')),
                ('changeRate', models.CharField(max_length=50, verbose_name='hourlyChangeRate')),
                ('changeType', models.CharField(max_length=50, verbose_name='hourlyChangeType')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EUROMonthly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='monthlyData')),
                ('value', models.CharField(max_length=50, verbose_name='monthlyValue')),
                ('changeRate', models.CharField(max_length=50, verbose_name='monthlyChangeRate')),
                ('changeType', models.CharField(max_length=50, verbose_name='monthlyChangeType')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='mainData')),
                ('value', models.CharField(max_length=50, verbose_name='mainValue')),
                ('changeRate', models.CharField(max_length=50, verbose_name='mainChangeRate')),
                ('changeType', models.CharField(max_length=50, verbose_name='mainChangeType')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
