# Generated by Django 3.0.4 on 2020-03-25 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_create_doctor_model'),
        ('medicines', '0001_create_medicine_model'),
        ('student', '0001_create_student_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('timestamp', models.DateTimeField(verbose_name='Date and time of visit')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor')),
                ('medicines_given', models.ManyToManyField(blank=True, to='medicines.Medicine')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Student')),
            ],
        ),
    ]