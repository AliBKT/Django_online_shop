# Generated by Django 4.0.2 on 2023-01-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_notes',
            field=models.CharField(blank=True, max_length=700),
        ),
    ]
