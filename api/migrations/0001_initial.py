# Generated by Django 2.1 on 2019-04-15 13:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=20)),
                ('sslcmarks', models.IntegerField(default=50)),
                ('pumarks', models.IntegerField(max_length=50)),
                ('degree', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('aggregate', models.IntegerField(default=35)),
                ('aboutme', models.TextField()),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None), blank=True, default=[], size=500)),
            ],
        ),
    ]
