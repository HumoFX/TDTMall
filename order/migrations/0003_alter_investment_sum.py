# Generated by Django 3.2.7 on 2021-10-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='sum',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
    ]
