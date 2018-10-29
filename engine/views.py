from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from rolepermissions.checkers import has_role
from django.contrib.auth.decorators import login_required
from CreditSols.roles import Customer
from personal.models import DuesInfo,PersonalAccount,CurrentLoan,CompletedLoan,PersonalInfo
from .forms import EligibilityForm
from .models import Score
from django.contrib import messages



# Create your views here.
@login_required
def eligibility_score(request):
    elig_amount = 0
    c_type = ""
    user = request.user
    if has_role(user,Customer):
        try:
            info_all = CurrentLoan.objects.filter(user = PersonalAccount.objects.all().filter(user=request.user)[0])
            savings = PersonalInfo.objects.filter(user = PersonalAccount.objects.all().filter(user=request.user)[0]).values("average_monthly_savings")[0]["average_monthly_savings"]
            info = (info_all).values_list("user",flat = True)
            length = len(info)
            emi_list = []
            for i in range(0,length):
                Loan_amount = (info_all).values("current_amount")[i]["current_amount"]
                Payment_period = (info_all).values("current_length")[i]["current_length"]
                Interest_rate = float(((info_all).values("current_interest")[i]["current_interest"])/100)
                emi = int((Loan_amount*pow((Interest_rate/12)+1,(Payment_period))*Interest_rate/12)/(pow(Interest_rate/12+1,(Payment_period)) - 1))
                emi_list.append(emi)
            total_emi = sum(emi_list)
            left_amount = int(savings-total_emi)
            if request.method == 'POST':
                eligibility_form = EligibilityForm(data=request.POST)
                if eligibility_form.is_valid():
                    tenure = int(eligibility_form.cleaned_data["tenure"])
                    rate = int(eligibility_form.cleaned_data["rate"])/1200
                    type = eligibility_form.cleaned_data["type"]
                    amount = int((left_amount*(pow(rate+1,tenure)-1))/(pow(rate+1,tenure)*rate))
                    amount1 = str(amount)
                    zeros = str(pow(10,(len(amount1)-1)))[1:]
                    if (int(amount1[1])<5):
                        amount2 = int(amount1[0] + zeros)
                    else:
                        amount2 = int(str(int(amount1[0])+1) + zeros)
                    elig_amount = f"{amount2:,d}"
                    c_type = type + " "
                else:
                    messages.error(request,eligibility_form.errors)
            else:
                eligibility_form = EligibilityForm()
            return render(request,'eligibility_score.html',{'eligibility_form':eligibility_form,'elig_amount':elig_amount,'c_type':c_type})
        except:
            return render(request,'eligibility_error.html')
    else:
        raise Http404


@login_required
def credit_score(request):
    user = request.user
    if has_role(user,Customer):
        try:
            info_all = DuesInfo.objects.filter(user = PersonalAccount.objects.all().filter(user=request.user)[0])
            info = (info_all).values_list("user",flat = True)
            score = 0
            if not info:
                length = 1
            else:
                length = len(info)
            Currently_Owned_Amount = []
            Previously_Owned_Amount = []
            Total_Number_Of_Overdues_in_Current_Loans = []
            Total_Overdue_Amount_of_Current_Loans = []
            Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans = []
            Total_Overdue_Amount_of_Current_Loans = []
            Total_Overdue_Amount_of_Completed_Loans = []
            Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans = []
            for i in range(0,length):
                Currently_Owned_Amount.append((info_all).values("Currently_Owned_Amount")[i]["Currently_Owned_Amount"])
                Previously_Owned_Amount.append((info_all).values("Previously_Owned_Amount")[i]["Previously_Owned_Amount"])
                Total_Number_Of_Overdues_in_Current_Loans.append((info_all).values("Total_Number_Of_Overdues_in_Current_Loans")[i]["Total_Number_Of_Overdues_in_Current_Loans"])
                Total_Overdue_Amount_of_Current_Loans.append((info_all).values("Total_Overdue_Amount_of_Current_Loans")[i]["Total_Overdue_Amount_of_Current_Loans"])
                Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans.append((info_all).values("Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans")[i]["Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans"])
                Total_Overdue_Amount_of_Current_Loans.append((info_all).values("Total_Overdue_Amount_of_Current_Loans")[i]["Total_Overdue_Amount_of_Current_Loans"])
                Total_Overdue_Amount_of_Completed_Loans.append((info_all).values("Total_Overdue_Amount_of_Completed_Loans")[i]["Total_Overdue_Amount_of_Completed_Loans"])
                Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans.append((info_all).values("Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans")[i]["Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans"])
            avg_Currently_Owned_Amount = (sum(Currently_Owned_Amount)/length)
            avg_Previously_Owned_Amount = (sum(Previously_Owned_Amount)/length)
            avg_Total_Number_Of_Overdues_in_Current_Loans = (sum(Total_Number_Of_Overdues_in_Current_Loans)/length)
            avg_Total_Overdue_Amount_of_Current_Loans = (sum(Total_Overdue_Amount_of_Current_Loans)/length)
            avg_Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans = (sum(Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans)/length)
            avg_Total_Overdue_Amount_of_Current_Loans = (sum(Total_Overdue_Amount_of_Current_Loans)/length)
            avg_Total_Overdue_Amount_of_Completed_Loans = (sum(Total_Overdue_Amount_of_Completed_Loans)/length)
            avg_Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans = (sum(Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans)/length)

            score = 696
            data = Score(user = PersonalAccount.objects.all().filter(user=request.user)[0],credit_score = score)
            data.save()
            return render(request,'credit_score.html',{"score":score})
        except:
            return render(request,'user_dashboard.html')
    else:
        raise Http404




# @login_required
# def credit_score(request):
#     user = request.user
#     if has_role(user,Customer):
#         info_all = DuesInfo.objects.filter(user = PersonalAccount.objects.all().filter(user=request.user)[0])
#         info = (info_all).values_list("user",flat = True)
#         if not info:
#             length = 1
#         else:
#             length = len(info)
#         Currently_Owned_Amount = []
#         Previously_Owned_Amount = []
#         Total_Number_Of_Overdues_in_Current_Loans = []
#         Total_Overdue_Amount_of_Current_Loans = []
#         Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans = []
#         Total_Overdue_Amount_of_Current_Loans = []
#         Total_Overdue_Amount_of_Completed_Loans = []
#         Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans = []
#         for i in range(0,length):
#             Currently_Owned_Amount.append((info_all).values("Currently_Owned_Amount")[i]["Currently_Owned_Amount"])
#             Previously_Owned_Amount.append((info_all).values("Previously_Owned_Amount")[i]["Previously_Owned_Amount"])
#             Total_Number_Of_Overdues_in_Current_Loans.append((info_all).values("Total_Number_Of_Overdues_in_Current_Loans")[i]["Total_Number_Of_Overdues_in_Current_Loans"])
#             Total_Overdue_Amount_of_Current_Loans.append((info_all).values("Total_Overdue_Amount_of_Current_Loans")[i]["Total_Overdue_Amount_of_Current_Loans"])
#             Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans.append((info_all).values("Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans")[i]["Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans"])
#             Total_Overdue_Amount_of_Current_Loans.append((info_all).values("Total_Overdue_Amount_of_Current_Loans")[i]["Total_Overdue_Amount_of_Current_Loans"])
#             Total_Overdue_Amount_of_Completed_Loans.append((info_all).values("Total_Overdue_Amount_of_Completed_Loans")[i]["Total_Overdue_Amount_of_Completed_Loans"])
#             Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans.append((info_all).values("Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans")[i]["Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans"])
#         avg_Currently_Owned_Amount = (sum(Currently_Owned_Amount)/length)
#         avg_Previously_Owned_Amount = (sum(Previously_Owned_Amount)/length)
#         avg_Total_Number_Of_Overdues_in_Current_Loans = (sum(Total_Number_Of_Overdues_in_Current_Loans)/length)
#         avg_Total_Overdue_Amount_of_Current_Loans = (sum(Total_Overdue_Amount_of_Current_Loans)/length)
#         avg_Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans = (sum(Maximum_Number_of_Days_Amount_is_Overdue_in_Current_Loans)/length)
#         avg_Total_Overdue_Amount_of_Current_Loans = (sum(Total_Overdue_Amount_of_Current_Loans)/length)
#         avg_Total_Overdue_Amount_of_Completed_Loans = (sum(Total_Overdue_Amount_of_Completed_Loans)/length)
#         avg_Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans = (sum(Maximum_Number_of_Days_Amount_is_Overdue_in_Completed_Loans)/length)
#         score = 696
#         data = Score(user = PersonalAccount.objects.all().filter(user=request.user)[0],credit_score = score)
#         data.save()
#         return render(request,'credit_score.html',{"score":score})
#     else:
#         raise Http404
