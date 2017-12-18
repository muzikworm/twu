# Generated by Django 2.1.dev20171213075741 on 2017-12-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
                ('aadhar', models.IntegerField(unique=True)),
                ('area', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
