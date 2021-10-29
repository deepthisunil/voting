from django.contrib import admin
from django.shortcuts import render,redirect
from .models import *


# Register your models here.

admin.site.register(voter_registration_table)
admin.site.register(candidate_registration_table)
admin.site.register(complaint)
admin.site.register(customuser)
admin.site.register(Upload_manifesto)


############################################################################## Admin Module #############################################################

############################# Load Admin Home ##############################

def load_admin_home(request):

    return render(request,'admin/admin_homepage.html')

############################ Approve Voters  ################################

def approve_voters(request):
    obj=voter_registration_table.objects.all().order_by('-id')

    

    

    if request.method == "POST" and 'update_id' in request.POST:
    
        get_update_id=request.POST.get("update_id")

        try:
            obj_update=voter_registration_table.objects.get(id=get_update_id)
            
        except voter_registration_table.DoesNotExist:
            obj_update=None

        status=request.POST.get("update")

        obj_update.status=status

        obj_update.save()
        

    if request.method == "POST" and 'remove_id' in request.POST:
        
        get_delete_id=request.POST.get("remove_id")

        try:
            obj_delete=voter_registration_table.objects.get(id=get_delete_id)
        
        except voter_registration_table.DoesNotExist:
            obj_delete=None

        

        obj_delete.delete()





    return render(request,'admin/admin_approve_voters.html',{"voter_details":obj})


############################ Approve Candidates  ################################

def approve_candidates(request):
    obj=candidate_registration_table.objects.all().order_by('-id')

    

    

    if request.method == "POST" and 'update_id' in request.POST:
    
        get_update_id=request.POST.get("update_id")

        try:
            obj_update=candidate_registration_table.objects.get(id=get_update_id)
            
        except candidate_registration_table.DoesNotExist:
            obj_update=None

        status=request.POST.get("update")

        obj_update.status=status

        obj_update.save()
        

    if request.method == "POST" and 'remove_id' in request.POST:
        
        get_delete_id=request.POST.get("remove_id")

        try:
            obj_delete=candidate_registration_table.objects.get(id=get_delete_id)
        
        except candidate_registration_table.DoesNotExist:
            obj_delete=None

        

        obj_delete.delete()

    if request.method == "POST" and 'upload_id' in request.POST:

        get_party_id = request.POST.get("upload_id")

        try:
            obj_symbol = candidate_registration_table.objects.get(id=get_party_id)

        except candidate_registration_table.DoesNotExist:
            obj_symbol = None

        img_scr=request.FILES["party_symbol"]


        obj_symbol.symbol_img=img_scr
        obj_symbol.save()



    return render(request,'admin/admin_approve_candidates.html',{"candidates_details":obj})


################################### Admin Add schedule ###################################

def add_schedules(request):
    obj = nomination_dates.objects.all()
    obj2=voting_schedule.objects.all()

    context={
        "nm_dates":obj,
        "vt_details":obj2
    }

    if request.method =="POST" and 'update_id' in request.POST:
        get_start_date=request.POST.get("nm_start_date")
        get_end_date = request.POST.get("nm_end_date")


        obj.delete()

        nomination_dates(start_date=get_start_date,end_date=get_end_date).save()

    if request.method == "POST" and 'update_id2' in request.POST:

        get_start_time=request.POST.get("vt_start_time")
        get_end_time = request.POST.get("vt_end_time")
        get_vt_date=request.POST.get("vt_date")
        obj2.delete()

        voting_schedule( start_time=get_start_time,end_time=get_end_time,voting_date=get_vt_date).save()





    return render(request,'admin/admin_add_schedule.html',context)


################################### Admin view Vote #######################################

def view_result(request):
    obj=candidate_registration_table.objects.all()

    return render(request,'admin/admin_view_results.html',{"candidates_details":obj})


################################## Admin add Result ########################################

def add_result(request):
    obj=candidate_registration_table.objects.filter(status="Approved")
    obj_result=result_table.objects.all()

    if request.method =="POST" and 'update_id' in request.POST:

        get_can_name=request.POST.get("cand_name")
        get_party=request.POST.get("p_name")
        get_count=request.POST.get("count")



        result_table(can_name=get_can_name,party_name=get_party,vote_count=get_count).save()

    if request.method == "POST" and 'remove_id' in request.POST:

        get_delete_id = request.POST.get("remove_id")
        print("##########################")
        print(get_delete_id)

        try:
            obj_delete = result_table.objects.get(id=get_delete_id)

        except result_table.DoesNotExist:
            obj_delete = None

        obj_delete.delete()

    context={
        "can_details":obj,
        "result_details":obj_result
    }

    return render(request,'admin/admin_add_result.html',context)

################################# Candidate  View Profile ####################################

def view_profile(request,can_id):
    obj=candidate_registration_table.objects.get(id=can_id)
    return render(request,'admin/candidate_profile.html',{"can_details":obj})

##########################################################################################################################################################
def complaint_view(request):
    data = complaint.objects.all()
    return render(request, 'admin/complaint.html',{'data':data})

##########################################################################


def complaint_reply(request,id=None):
    data = complaint.objects.get(id=id)
    print(data)
    if request.method=='POST':
        user_reply=request.POST.get('reply')
        data.reply=user_reply
        data.save()
        return redirect('complaint_view')


    return render(request,'admin/complaint_reply.html')

################################################################################