from django.shortcuts import render,redirect
from .forms import *
from .models import *


def phome(request):
    return render(request, 'party/party_home.html')
def PartyRegistrationView(request):
    if request.method=='POST':
        form =PartyRegistration(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_party = True
            form.save()
            return redirect('login_page')
    else:
        form = PartyRegistration(request.POST, request.FILES)
    return render(request,'party/party_registration.html',{'form':form})
########################## TO VIEW THE PARTY REGISTRATION FORM ##############################################


def CreateManifestoView(request):
    if request.method =='POST':
        form = partyUploadManifestoFORM(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_party = request.user
            form.save()
        return render(request,'party/party_home.html')
    else:
        form = partyUploadManifestoFORM(request.POST, request.FILES)
    return render(request,'party/upload_party_manifesto.html',{'form':form})

##############################TO CREATE MANIFEST UPLOAD FORM ##############################################################



def PARTYview_result(request):

    obj = result_table.objects.all().order_by('-vote_count')
    return render(request,'party/view_result.html',{"result_details":obj})
