# Generated by Django 2.0.6 on 2018-06-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='phone',
            field=models.PositiveSmallIntegerField(blank=True, default='0', max_length=13),
        ),
        migrations.AlterField(
            model_name='completedloan',
            name='comp_amount',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='Amount (rupees)'),
        ),
        migrations.AlterField(
            model_name='completedloan',
            name='comp_bank',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Bank Name'),
        ),
        migrations.AlterField(
            model_name='completedloan',
            name='comp_interest',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='Ratre of Interest'),
        ),
        migrations.AlterField(
            model_name='completedloan',
            name='comp_length',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='Length (months)'),
        ),
        migrations.AlterField(
            model_name='currentloan',
            name='current_amount',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='Amount (rupees)'),
        ),
        migrations.AlterField(
            model_name='currentloan',
            name='current_bank',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Bank Name'),
        ),
        migrations.AlterField(
            model_name='currentloan',
            name='current_duration',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='Duration (months)'),
        ),
        migrations.AlterField(
            model_name='currentloan',
            name='current_interest',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='Rate of Interest'),
        ),
        migrations.AlterField(
            model_name='currentloan',
            name='current_length',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='Length (months)'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='aadhar_number',
            field=models.CharField(blank=True, default='', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='address',
            field=models.TextField(blank=True, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='average_monthly_savings',
            field=models.PositiveSmallIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='date_of_birth',
            field=models.DateField(blank=True, default='01/02/1997', null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='monthly_income',
            field=models.PositiveSmallIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='pan_number',
            field=models.CharField(blank=True, default='', max_length=10, unique=True),
        ),
    ]
