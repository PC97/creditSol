# Generated by Django 2.0.6 on 2018-07-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20180709_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='month',
            field=models.TextField(default='July', editable=False),
        ),
    ]