# Generated by Django 5.2 on 2025-04-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmg', '0011_newsimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
        migrations.RemoveField(
            model_name='property',
            name='status',
        ),
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_size',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.CharField(max_length=32),
        ),
    ]
