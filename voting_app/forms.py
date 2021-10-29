from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm




####################################################################### Voter Registration Form ##################################################################

class voter_registration_form(forms.ModelForm):

    class Meta:
        model=voter_registration_table
        fields=['name','dob','voter_img','gender','email','phone','address','add_no','caste','religion']



##################################################################################################################################################################

####################################################################### Candidate Registration Form ##################################################################

class candidate_registration_form(forms.ModelForm):

    class Meta:
        model=candidate_registration_table
        fields=['name','job','party_name','username']



##################################################################################################################################################################
class complaint_form(forms.ModelForm):

    class Meta:
        model=complaint
        fields=('complaint',)
############################################################################################
class complaint_reply(forms.ModelForm):

     class Meta:
         model=complaint
         fields=('reply',)
###########################################################################################
class PartyRegistration(UserCreationForm):

     class Meta(UserCreationForm.Meta):
         model=customuser
         fields=('username','password1','password2','place','address','email','phone','image')
##############################################################################################

class partyUploadManifestoFORM(forms.ModelForm):

    class Meta:
        model=Upload_manifesto
        fields=('image','text_something')