# Generated by Django 3.1.6 on 2021-02-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0003_auto_20210215_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
