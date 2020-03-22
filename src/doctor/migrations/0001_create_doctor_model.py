# Generated by Django 3.0.4 on 2020-03-22 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import doctor.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=doctor.utils.image_upload_util, validators=[doctor.utils.image_file_size_validator], verbose_name='Display Picture')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('about', models.TextField(verbose_name='About The Doctor')),
                ('education', models.TextField(verbose_name='Education Details')),
                ('available_description', models.TextField(verbose_name='Availability')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
