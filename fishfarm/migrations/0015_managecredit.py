# Generated by Django 4.0.5 on 2022-07-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0014_delete_managecredit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditYear', models.TextField()),
                ('totalCredit', models.FloatField()),
            ],
        ),
    ]