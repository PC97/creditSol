# Generated by Django 2.0.6 on 2018-07-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_auto_20180702_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
