# Generated by Django 3.0.8 on 2020-07-06 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]