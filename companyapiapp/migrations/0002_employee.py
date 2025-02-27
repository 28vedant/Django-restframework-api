# Generated by Django 5.0.4 on 2024-04-13 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('Manager', 'Manager'), ('Developer', 'Developer'), ('Tester', 'Tester')], max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapiapp.company')),
            ],
        ),
    ]
