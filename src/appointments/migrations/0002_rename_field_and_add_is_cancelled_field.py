# Generated by Django 3.0.4 on 2020-03-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_create_appointment_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Doctor',
            new_name='doctor',
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
