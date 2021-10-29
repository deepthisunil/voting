from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login
######################################################################### Sign In ##############################################################################

####################### Login Page ########################

def display_login_page(request):

    if request.method == "POST":
        get_username=request.POST.get("username")
        get_password=request.POST.get("password")
        print(get_username)
        print(get_password)


        try:
            user = authenticate(username=get_username, password=get_password)
            print('user',user)
            login(request, user)

            # print(request.user.is_party)
            # if request.user.is_party:
            #     return render(request,'party/party_home.html')
        except:
            print('error')
        if get_username == 'admin' and get_password=='admin':

            return redirect('admin_home')
        elif voter_registration_table.objects.filter(username=get_username,password=get_password,status="Approved").exists():
            request.session['name']=get_username
            print("@@@@@@@@@@@@@@@")
            print(request.session['name'])
            return  redirect('home_user')

        else:
            if request.user.is_party:
                return render(request,'party/party_home.html')

            return render(request,'error.html')



    return render(request,'login.html')

###########################################################################################################################################################

#
# def userview(request):
#     print(request.user.is_party)
#     get_username=request.POST.get("username")
#     print(get_username)
#     if request.user.is_party:
#         return render(request,'party/party_home.html')
#     if request.user.is_superuser:
#         return redirect('admin_home')
#     elif voter_registration_table.objects.filter(username=get_username, password=get_password,
#                                                  status="Approved").exists():
#         request.session['name'] = get_username
#         print("@@@@@@@@@@@@@@@")
#         print(request.session['name'])
#         return redirect('home_user')
#
#
