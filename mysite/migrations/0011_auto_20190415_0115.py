# Generated by Django 2.1.1 on 2019-04-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20190415_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='male', max_length=7),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('junior', 'junior'), ('graduate', 'graduate'), ('freshman', 'freshman'), ('sophomore', 'sophomore'), ('senior', 'senior')], default='freshman', max_length=20),
        ),
    ]
