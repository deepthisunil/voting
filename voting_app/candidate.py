from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.utils.crypto import get_random_string
from django.contrib import messages
import random
############################################################################ Candidate Module #############################################################

############################# candidate search ######################

def search(request):

    if request.method == "POST" and 'search_btn' in request.POST:

        get_id=request.POST.get("voter_id")

        if voter_registration_table.objects.filter(username=get_id).exists():

            return  redirect('registration_page_candidate',get_id)

        else:
            messages.info(request, "No details found")

    return render(request,'search.html')



############################# Candidate Registration ################

def load_candidate_registration(request,req_id):

    obj=voter_registration_table.objects.get(username=req_id)




    if request.method == "POST":
    
        
        form =candidate_registration_form(request.POST,request.FILES)

        if form.is_valid():
            obj_form=form.save(commit=True)
            obj_form.status="Not Approved"
            x = random.randint(10000, 100000)
            get_app_no="APP"+str(x)
            obj_form.application_no=get_app_no
            obj_form.vote_count=0
            obj_form.symbol_img="img"
            obj_form.user_id=obj

             
            obj_form.save()
            obj_details=candidate_registration_table.objects.all().last()
            context={
                "details":obj_details
            }
            messages.info(request,"Your Application have been submitted sucessfully.Please Note the Application number for future use. ")
            return render(request,'message.html',context)
        else:
            form =candidate_registration_form()

    return render(request,'candidate.html',{"can_details":obj})



########################## View Nomination Status ########################

def view_nomination_status(request):



    if request.method == "POST":


        get_app_no= request.POST.get("app_no")

        if candidate_registration_table.objects.filter(application_no=get_app_no).exists():

            obj_details=candidate_registration_table.objects.get(application_no=get_app_no)
            messages.info(request,"Your Application status")



            context={

                "application_status":obj_details
                }

            return render(request,'candidate_view_nomination.html',context)
        else:

            messages.error(request,"You are not a registered candidate")

           



            return render(request,'candidate_view_nomination.html')





    return render(request,'candidate_view_nomination.html')



#####################################################################################################################################################