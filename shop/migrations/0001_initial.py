# Generated by Django 5.0.6 on 2024-05-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
