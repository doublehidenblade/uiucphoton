# Generated by Django 2.1.1 on 2019-04-18 07:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_auto_20190418_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to='media', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('sophomore', 'sophomore'), ('junior', 'junior'), ('senior', 'senior'), ('graduate', 'graduate'), ('freshman', 'freshman')], default='', max_length=20),
        ),
    ]
