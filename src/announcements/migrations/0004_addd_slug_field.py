# Generated by Django 3.0.4 on 2020-03-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_alter_datetime_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
