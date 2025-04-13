# Generated by Django 5.2 on 2025-04-13 02:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmg', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DisplayImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('position', models.IntegerField(default=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='bmg.display')),
            ],
            options={
                'verbose_name': 'Display Image',
                'verbose_name_plural': 'Display Images',
                'ordering': ['position', 'created_at'],
            },
        ),
    ]
