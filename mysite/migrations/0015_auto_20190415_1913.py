# Generated by Django 2.1.1 on 2019-04-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_auto_20190415_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='male', max_length=7),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('freshman', 'freshman'), ('junior', 'junior'), ('senior', 'senior'), ('graduate', 'graduate'), ('sophomore', 'sophomore')], default='freshman', max_length=20),
        ),
    ]
