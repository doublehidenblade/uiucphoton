# Generated by Django 2.1.1 on 2019-04-18 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_auto_20190418_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('graduate', 'graduate'), ('senior', 'senior'), ('freshman', 'freshman'), ('sophomore', 'sophomore'), ('junior', 'junior')], default='', max_length=20),
        ),
    ]