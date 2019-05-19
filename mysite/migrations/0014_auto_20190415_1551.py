# Generated by Django 2.1.1 on 2019-04-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20190415_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='embedcode',
            field=models.URLField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('sophomore', 'sophomore'), ('senior', 'senior'), ('graduate', 'graduate'), ('freshman', 'freshman'), ('junior', 'junior')], default='freshman', max_length=20),
        ),
    ]
