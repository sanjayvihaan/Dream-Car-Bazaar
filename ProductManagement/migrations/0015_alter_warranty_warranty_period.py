# Generated by Django 4.1.3 on 2024-10-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0014_alter_cardetails_total_air_bag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='warranty_period',
            field=models.CharField(max_length=10),
        ),
    ]
