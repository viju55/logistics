# Generated by Django 2.0 on 2019-09-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transporter', '0002_auto_20190912_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transporter',
            name='confirm_password',
        ),
    ]