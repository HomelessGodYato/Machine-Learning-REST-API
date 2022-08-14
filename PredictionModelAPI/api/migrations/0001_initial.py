# Generated by Django 4.1 on 2022-08-13 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.IntegerField()),
                ('body', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('engine_v', models.FloatField()),
                ('engine_type', models.IntegerField()),
                ('registration', models.BooleanField()),
                ('year', models.IntegerField()),
                ('model', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PredictedPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_price', models.FloatField()),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_id', to='api.requestedfeatures')),
            ],
        ),
    ]