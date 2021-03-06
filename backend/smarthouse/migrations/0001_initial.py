# Generated by Django 3.1.7 on 2021-02-24 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=16)),
                ('unit', models.CharField(max_length=8)),
                ('classification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sensors', to='smarthouse.classification')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sensors', to='smarthouse.room')),
            ],
        ),
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indications', to='smarthouse.sensor')),
            ],
        ),
    ]
