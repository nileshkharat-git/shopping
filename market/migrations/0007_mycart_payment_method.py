# Generated by Django 3.1.2 on 2020-11-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20201101_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='payment_method',
            field=models.CharField(max_length=100, null=True),
        ),
    ]