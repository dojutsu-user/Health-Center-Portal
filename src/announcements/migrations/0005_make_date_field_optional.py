# Generated by Django 3.0.4 on 2020-03-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0004_addd_slug_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(blank=True, null=True),
        ),
    ]
