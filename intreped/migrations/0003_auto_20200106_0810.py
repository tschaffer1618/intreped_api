# Generated by Django 3.0.1 on 2020-01-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intreped', '0002_auto_20191220_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]