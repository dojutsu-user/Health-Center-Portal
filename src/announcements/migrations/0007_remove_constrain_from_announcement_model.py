# Generated by Django 3.0.4 on 2020-03-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0006_add_constraint_to_announcement'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='announcement',
            name='active_post_must_have_date',
        ),
    ]
