# Generated by Django 3.0.4 on 2020-03-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_integrate_ckeditor_to_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(),
        ),
    ]
