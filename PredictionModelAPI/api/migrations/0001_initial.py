# Generated by Django 4.1 on 2022-09-05 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JSONFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestedFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carat', models.FloatField()),
                ('cut', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('clarity', models.CharField(max_length=25)),
                ('depth', models.FloatField()),
                ('table', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='api.jsonfile')),
            ],
        ),
        migrations.CreateModel(
            name='PredictedPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_price', models.FloatField()),
                ('features_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prediction', to='api.requestedfeatures')),
            ],
        ),
        migrations.CreateModel(
            name='MLModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default='', max_length=250)),
                ('model_score', models.FloatField(default=0)),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ml_model', to='api.jsonfile')),
                ('prediction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ml_model', to='api.predictedprice')),
            ],
        ),
    ]