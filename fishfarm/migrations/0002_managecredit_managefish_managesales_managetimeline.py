# Generated by Django 4.0.5 on 2022-07-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCredit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ManageFish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishName', models.TextField()),
                ('fishCount', models.IntegerField()),
                ('fishSold', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ManageSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishSales', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ManageTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvestTime', models.DateField()),
            ],
        ),
    ]