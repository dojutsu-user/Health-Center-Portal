# Generated by Django 3.0.4 on 2020-03-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_create_medicine_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
