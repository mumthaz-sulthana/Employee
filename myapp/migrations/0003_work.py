# Generated by Django 5.0.6 on 2024-07-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('created', 'created'), ('wip', 'wip'), ('completed', 'completed'), ('due', 'due')], default='created', max_length=30)),
            ],
        ),
    ]
