# Generated by Django 2.2.9 on 2020-01-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_federal'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitor',
            fields=[
                ('veh_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('apartment', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=50)),
                ('veh_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='resident',
            old_name='car_model',
            new_name='veh_type',
        ),
    ]
