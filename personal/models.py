from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from business.models import BusinessAccount
from datetime import datetime


# Create your models here.
class PersonalAccount(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.user.username


class PersonalInfo(models.Model):
    user = models.OneToOneField(
        PersonalAccount,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER,null=True)
    phone = models.CharField(max_length=11,null=True,unique = True)
    aadhar_number = models.CharField(max_length=12,unique=True,null=True)
    pan_number = models.CharField(max_length=10,unique=True,null=True)
    address = models.TextField(unique=True,null=True)
    date_of_birth = models.DateField(null=True,blank=True)
    monthly_income = models.PositiveSmallIntegerField(null=True)
    average_monthly_savings = models.PositiveSmallIntegerField(null=True)
    def __str__(self):
        return self.user.user.username

@receiver(post_save, sender=PersonalAccount)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PersonalInfo.objects.create(user=instance)
@receiver(post_save, sender=PersonalAccount)
def save_user_profile(sender, instance, **kwargs):
    instance.personalinfo.save()


class CurrentLoan(models.Model):
    user = models.ForeignKey(
        PersonalAccount,
        on_delete=models.CASCADE,
    )
    current_bank = models.CharField("Bank Name",max_length = 20,null=True)
    current_amount = models.PositiveSmallIntegerField("Amount (rupees)",null=True)
    current_length = models.PositiveSmallIntegerField("Length (months)",null=True)
    current_interest = models.PositiveSmallIntegerField("Rate of Interest",null=True)
    current_duration = models.PositiveSmallIntegerField("Duration (months)",null=True)
    def __str__(self):
        return self.user.user.username


class CompletedLoan(models.Model):
    user = models.ForeignKey(
        PersonalAccount,
        on_delete=models.CASCADE,
    )
    comp_bank = models.CharField("Bank Name",max_length = 20,null=True)
    comp_amount = models.PositiveSmallIntegerField("Amount (rupees)",null=True)
    comp_length = models.PositiveSmallIntegerField("Length (months)",null=True)
    comp_interest = models.PositiveSmallIntegerField("Rate of Interest",null=True)
    def __str__(self):
        return self.user.user.username


current_month = (datetime.now()).strftime("%B")
class DuesInfo(models.Model):
    user = models.ForeignKey(
        PersonalAccount,
        on_delete=models.CASCADE,
    )
    bank = models.ForeignKey(
        BusinessAccount,
        on_delete=models.CASCADE,
        null = True,
    )
    STATUS = (
        ('P', 'Pending'),
        ('W', 'Written Off'),
    )
    Currently_Owned_Amount = models.PositiveIntegerField(null=True)
    Previously_Owned_Amount = models.PositiveIntegerField(null=True)
    Total_Number_Of_Overdues_in_Current_Loans = models.PositiveIntegerField(null=True)
    Total_Overdue_Amount_of_Current_Loans = models.PositiveIntegerField(null=True)
    Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans = models.PositiveIntegerField(null=True)
    Status = models.CharField(max_length=1, choices=STATUS,null=True)
    Total_Overdue_Amount_of_Current_Loans = models.PositiveIntegerField(null=True)
    Total_Overdue_Amount_of_Completed_Loans = models.PositiveIntegerField(null=True)
    Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans = models.PositiveIntegerField(null=True)
    class Meta:
        unique_together = (("user","bank"),)
    def __str__(self):
        return "{0} ({1}) [{2}]".format(self.user.user.username, self.bank.user.first_name,current_month)
