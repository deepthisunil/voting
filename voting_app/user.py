from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.utils.crypto import get_random_string
from django.contrib import messages
import  random

from datetime import datetime
from datetime import date
# Create your views here.


####################################################################### User Module ########################################################################

######################## User Registration #################

def display_registration_page(request):

    if request.method == "POST":

        get_phone=request.POST.get("phone")

        form =voter_registration_form(request.POST,request.FILES)

        if form.is_valid():
            obj=form.save(commit=True)
            obj.status="Not Approved"
            x = random.randint(10000, 100000)
            get_username="VID"+str(x)
            obj.username=get_username
            obj.password=get_phone
            obj.poll_status=0
            obj.save()
            obj_details=voter_registration_table.objects.all().last()
            context={
                "details":obj_details
            }

            messages.info(request,"Your Login Credentials ")
            return render(request,'user_registration.html',context)
        else:
            form =voter_registration_form()
            messages.error(request, "Registration not successfull please try again! ")

    return  render(request,'user_registration.html')


######################## user home ##########################

def user_home(request):


    obj_user=voter_registration_table.objects.get(username=request.session["name"])
    obj_schedule=voting_schedule.objects.all().last()
    obj_nomination=nomination_dates.objects.all().last()



    today = date.today()
    now = datetime.now().time()
    current_time = now.strftime("%H:%M:%S")


    print("$$$$$$$$$$$$$$$$$$")
    print(today)
    print(now)
    print(current_time)
    print(type(now))
    print(type(current_time))
    print(type(obj_schedule.start_time))


    if request.method == "POST" and 'vote_btn' in request.POST:

        if obj_user.poll_status == 1:
            messages.error(request,'You have already Voted')

        elif today != obj_schedule.voting_date:
            messages.error(request, 'Voting link not available.')

        elif now < obj_schedule.start_time or now > obj_schedule.end_time:

            messages.error(request,"Voting link expired")


        else:
            return redirect('step2')
    if request.method == "POST" and 'nom_btn' in request.POST:

        if today < obj_nomination.start_date or today >obj_nomination.end_date:
            messages.error(request, 'Nomination link not available.')

        else:
            return redirect('choice_select')
    # return render(request,'userhome.html')
    return render(request,'user/user_homepage.html')
def voteview(request):
    obj_user = voter_registration_table.objects.get(username=request.session["name"])
    obj_schedule = voting_schedule.objects.all().last()
    obj_nomination = nomination_dates.objects.all().last()

    today = date.today()
    now = datetime.now().time()
    current_time = now.strftime("%H:%M:%S")

    print("$$$$$$$$$$$$$$$$$$")
    print(today)
    print(now)
    print(current_time)
    print(type(now))
    print(type(current_time))
    print(type(obj_schedule.start_time))
    if obj_user.poll_status == 1:
        messages.error(request, 'You have already Voted')

    elif today != obj_schedule.voting_date:
        messages.error(request, 'Voting link not available.')

    elif now < obj_schedule.start_time or now > obj_schedule.end_time:

        messages.error(request, "Voting link expired")


    else:
        return redirect('step2')
    # return redirect('step2')
    return render(request, 'user/user_homepage.html')
def niminationview(request):
    obj_user = voter_registration_table.objects.get(username=request.session["name"])
    obj_schedule = voting_schedule.objects.all().last()
    obj_nomination = nomination_dates.objects.all().last()

    today = date.today()
    now = datetime.now().time()
    current_time = now.strftime("%H:%M:%S")

    print("$$$$$$$$$$$$$$$$$$")
    print(today)
    print(now)
    print(current_time)
    print(type(now))
    print(type(current_time))
    print(type(obj_schedule.start_time))
    if today < obj_nomination.start_date or today > obj_nomination.end_date:
        messages.error(request, 'Nomination link not available.')

    else:
        return redirect('choice_select')
    return redirect('choice_select')
    # return render(request, 'user/user_homepage.html')
#################### choice #################################

def select_choice(request):

    if request.method == "POST" and 'submit_btn' in request.POST:
        return redirect('can_search')
    if request.method == "POST" and 'view_btn' in request.POST:
        return redirect('view_candidate_nomination')
    return render(request,'voter_choice3.html')

################### view result #############################

def view_result(request):
    obj = result_table.objects.all().order_by('-vote_count')
    return render(request,'user_view_result.html',{"result_details":obj})
#######################################################################


def uhome(request):
    return render(request, 'user/user_homepage.html')



########################################################################################################################################################
def Createcomplaint(request):
    if request.method =='POST':
        form =complaint_form(request.POST)
        cr_user = voter_registration_table.objects.get(username=request.session["name"])
        if form.is_valid():
            form = form.save(commit=False)
            form.sender =cr_user
            form.save()

            return redirect('complaint')
    else:
        form = complaint_form()
    return render(request,'user/complaint.html',{'form':form})

#######################################################################################################
def user_complaint_view(request):
    cr_user = voter_registration_table.objects.get(username=request.session["name"])

    data = complaint.objects.filter(sender=cr_user)
    return render(request, 'user/complaintview.html',{'data':data})

##########################################################################################################




