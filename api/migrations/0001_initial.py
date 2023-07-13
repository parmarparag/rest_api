# Generated by Django 4.2.2 on 2023-07-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('types', models.CharField(choices=[('Full Time', 'Full time'), ('Part Time', 'Part-time'), ('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile Phones', 'Mobile Phones')], max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]