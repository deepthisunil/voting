from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



############################################################################## User Module ###################################################

############################## Voter Registration table ####################

class voter_registration_table(models.Model):

    name=models.CharField(max_length=250)
    voter_img=models.ImageField(upload_to='voters_image')
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=100)
    add_no = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250,unique=True)
    status=models.CharField(max_length=250)
    username=models.CharField(max_length=250,unique=True)
    password=models.CharField(max_length=250,unique=True)
    caste=models.CharField(max_length=250)
    religion=models.CharField(max_length=250)
    poll_status=models.IntegerField(null=True)





########################################################################################################################################

############################################################################## Candidate Module ###################################################

############################## Candidate Registration table ####################

class candidate_registration_table(models.Model):

    name=models.CharField(max_length=250)
    party_name=models.CharField(max_length=250)
    symbol_img=models.ImageField(upload_to='party_symbols')
    job=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    application_no=models.CharField(max_length=250)
    vote_count=models.IntegerField(null=True)
    user_id=models.ForeignKey(voter_registration_table,on_delete=models.CASCADE,null=True)




########################################################################################################################################

############################################################################## Admin #################################################################

###########################  Nomination Schedule ###############################

class nomination_dates(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()

###########################  Voting Schedule ###############################

class voting_schedule(models.Model):
    start_time=models.TimeField()
    end_time=models.TimeField()
    voting_date=models.DateField()

########################## Result Table #######################################

class result_table(models.Model):
    can_name=models.CharField(max_length=250)
    party_name=models.CharField(max_length=250)
    vote_count=models.IntegerField()



################################################################################################################################################


class complaint(models.Model):
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100,null=True, blank=True)
    sender = models.ForeignKey(voter_registration_table,on_delete=models.CASCADE, null=True)



############################################################################################

class customuser(AbstractUser):
    is_party=models.BooleanField(default=False)
    place=models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=250,null=True)
    email = models.CharField(max_length=250,null=True)
    phone = models.CharField(max_length=250, unique=True,null=True)
    image = models.ImageField(upload_to='images',null=True)

# ##########################################################################################

class Upload_manifesto(models.Model):
    is_party = models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images', null=True)
    text_something = models.CharField(max_length=250,null=True)

#####################################################################################################333