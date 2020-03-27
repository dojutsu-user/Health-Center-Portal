# Generated by Django 3.0.4 on 2020-03-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_make_image_field_non_empty'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Is The Doctor Available?'),
        ),
    ]
