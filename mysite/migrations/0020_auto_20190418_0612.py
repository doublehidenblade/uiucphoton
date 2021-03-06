# Generated by Django 2.1.1 on 2019-04-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_auto_20190418_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=196),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='person',
            name='major',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('sophomore', 'sophomore'), ('senior', 'senior'), ('freshman', 'freshman'), ('graduate', 'graduate'), ('junior', 'junior')], default='', max_length=20),
        ),
    ]
