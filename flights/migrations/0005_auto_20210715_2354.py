# Generated by Django 3.1.5 on 2021-07-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]
