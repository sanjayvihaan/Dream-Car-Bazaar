# Generated by Django 4.1.3 on 2024-10-18 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0018_alter_cardetails_status_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='viewed_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_detail', to='ProductManagement.cardetails'),
        ),
    ]
