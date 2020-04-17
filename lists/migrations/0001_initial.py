# Generated by Django 2.1.5 on 2020-04-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('state', models.TextField()),
                ('available_date', models.DateField()),
                ('image', models.ImageField(upload_to='image/')),
                ('hotel_name', models.CharField(max_length=100)),
            ],
        ),
    ]
