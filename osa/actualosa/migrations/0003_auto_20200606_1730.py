# Generated by Django 3.0.7 on 2020-06-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualosa', '0002_auto_20200606_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='instrumentResponse',
            field=models.CharField(default='See the instrument response here', max_length=255),
        ),
    ]
