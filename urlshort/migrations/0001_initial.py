# Generated by Django 3.1.5 on 2021-01-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=700)),
                ('short_url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('time_date_created', models.DateTimeField()),
            ],
        ),
    ]