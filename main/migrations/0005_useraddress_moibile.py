# Generated by Django 3.1.2 on 2020-11-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_useraddress_usedefault'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='moibile',
            field=models.CharField(max_length=10, null=True, verbose_name='Mobile'),
        ),
    ]
