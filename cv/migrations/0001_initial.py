# Generated by Django 2.2.14 on 2020-08-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('emailAddress', models.CharField(max_length=100)),
                ('aboutMe', models.TextField()),
            ],
        ),
    ]
