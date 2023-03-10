# Generated by Django 3.2 on 2021-05-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ap_id', models.AutoField(primary_key=True, serialize=False)),
                ('ap_patient_fname', models.CharField(max_length=15)),
                ('ap_patient_lname', models.CharField(max_length=15)),
                ('ap_patient_email', models.EmailField(max_length=20)),
                ('ap_patient_number', models.CharField(max_length=10)),
                ('cancer_type', models.CharField(max_length=15)),
                ('ap_time', models.DateTimeField()),
                ('h_name', models.CharField(max_length=20)),
                ('d_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_fname', models.CharField(max_length=15)),
                ('p_lname', models.CharField(max_length=15)),
                ('p_email', models.EmailField(max_length=20)),
                ('ap_label', models.TextField()),
            ],
        ),
    ]
