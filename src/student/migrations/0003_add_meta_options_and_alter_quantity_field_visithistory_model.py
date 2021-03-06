# Generated by Django 3.0.4 on 2020-03-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_create_visit_history_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visithistory',
            options={'verbose_name_plural': 'Visit histories'},
        ),
        migrations.AlterField(
            model_name='visithistory',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, verbose_name='Quantity'),
        ),
    ]
