# Generated by Django 2.0.3 on 2022-01-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('phone', models.CharField(max_length=100)),
                ('age', models.DurationField(default=None)),
                ('voter_no', models.CharField(default=829742, max_length=300)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'voter',
            },
        ),
    ]