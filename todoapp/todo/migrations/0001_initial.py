# Generated by Django 5.0 on 2024-01-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
