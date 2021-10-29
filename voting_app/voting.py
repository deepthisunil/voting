from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib import messages
from .detection import *

####################################################### OTP sending #########################################################################

def send_otp(request):


    if request.method == "POST" and 'send_btn' in request.POST:

    
        OTP = random.randint(10000,100000)
        print("###########################")
        print(OTP)
        request.session['otp']=OTP
        x=request.session['name']
        obj=voter_registration_table.objects.get(username=x)
        reciept_email=obj.email
        subject = 'One Time Password'
        message = 'Hi this is One Time Password is\t' +str(OTP)+  '\t for continue the voting process.\n'+'Do not share the OTP with any one.\n'+'Thank You'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [reciept_email ]
        send_mail( subject, message, email_from, recipient_list )

        return redirect('otp_check')

        


    

    return render(request,'voter_choice.html')




    

###############################################################################################################################################

####################################################### Checking OTP ##########################################################################

def check_otp(request):

    if request.method =="POST" and 'check_btn' in request.POST:
        get_otp=request.POST.get("otp")

        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        #print(get_otp)

        #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        #print(OTP)
        x=request.session['otp']
        #print("@@@@@@@@@@@@@@@@@@@@@@")
        #print(x)
        if int(get_otp) == int(x) :
                    
            return redirect('voting_page_load')
        else:
            messages.error(request,'The entered OTP is not correct. Please try again.')

    if request.method =="POST" and 'resnd_btn' in request.POST:

        return redirect('otp_send')
    return render(request,'check_otp.html')

##############################################################################################################################################

####################################################### choice page ##########################################################################

def load_choice(request):

    if request.method == "POST" and 'next_btn' in request.POST:
        x=request.session['name']
        obj=voter_registration_table.objects.get(username=x)

        print("############ image path ##################")
        print(obj.voter_img)

        print("$$$$$$$$$$$$$$$$$$$$$")
        img_scr='media/'+str(obj.voter_img)
        print(img_scr)

        voter_name=obj.name
        print("&&&&&&&&&&&&&&&&&")
        print(voter_name)

        name=get_name(img_scr,voter_name)

        print("%%%%% the result name %%%%%%%%%%%%%%%%%")
        print(name)

        if name == voter_name:
            return  redirect('otp_send')
        else:
            return redirect('login_page')


    return render(request,'voter_choice2.html')

##############################################################################################################################################


######################################################### Voting Page ########################################################################

def load_voting_page(request):

    obj=candidate_registration_table.objects.filter(status="Approved")

    if request.method == "POST":

        req_id=request.POST.get("vote")

        obj_update=candidate_registration_table.objects.get(id=req_id)
        
        obj_update.vote_count=obj_update.vote_count+1
        obj_update.save()
        return redirect('user_final',req_id)


    return render(request,'voting_page.html',{"canditates_details":obj})


############################# final page display #########################

def user_final_page(request,get_id):

    x = request.session['name']
    obj_user = voter_registration_table.objects.get(username=x)
    obj_candidate=candidate_registration_table.objects.get(id=get_id)

    context={
        "user_details":obj_user,
        "can_details":obj_candidate
    }

    if request.method =="POST":
        obj_user.poll_status=1
        obj_user.save()
        return redirect('msg_final')
    return render(request,'final_page.html',context)

############################## Final Message Page ###############################

def print_msg(request):

    messages.success(request,'Your Voting is complete!.')

    return render(request,'message2.html')


###############################################################################################################################################

