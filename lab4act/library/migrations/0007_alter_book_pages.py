# Generated by Django 3.2.4 on 2021-06-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20210621_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
