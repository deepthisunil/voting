"""online_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import user
from .import admin
from .import signin
from .import candidate
from .import voting
from .import party

urlpatterns = [

    ################################################################### Admin Module ###########################################################

    ################################ Admin Homepage Url #####################################

    path('load_admin_page',admin.load_admin_home,name="admin_home"),

    ################################ Admin View Voters Details Url ######################

    path('admin_approve_voters',admin.approve_voters,name="voters_approve"),

    ################################ Admin View Candidate Details Url ######################

    path('admin_approve_candidates',admin.approve_candidates,name="candidates_approve"),

    ################################ Admin View result Url #################################

    path('admin_view_results',admin.view_result,name="result_view"),

    ################################ Admin Add schedule #####################################

    path('admin_add_schedule',admin.add_schedules,name="schedule_add"),

    ################################ Admin add Result #######################################

    path('admin_add_result',admin.add_result,name="result_add"),

    ############################### Admin view can profile ##################################

    path('admin_view_profile<int:can_id>',admin.view_profile,name="profile_view"),

    ############################################################################################################################################

    ########################################################################  Voting Page ############################################################

    ############################ send OTP url #####################

    path('voter_select_choice',voting.send_otp,name="otp_send"),

    ############################ check OTP url #####################

    path('voter_otp_check',voting.check_otp,name="otp_check"),

    ############################ select choice url #################

    path('voter_verification_step',voting.load_choice,name="step2"),

    ############################ Loading Voting Page ###############

    path('display_voting_page',voting.load_voting_page,name="voting_page_load"),

    ############################ Final Page display ###################

    path('display_final_page<int:get_id>',voting.user_final_page,name="user_final"),

    ############################ Final Message ############################

    path('display_final_message',voting.print_msg,name="msg_final"),

    #############################################################################################################################################

    #################################################################### User Module ###########################################################

    ################################ User Registration Page Url ###############################

    path('User_registration_page', user.display_registration_page,name="registration_page_user"),

    ################################ User home ################################################

    path('user_home_display',user.user_home,name="home_user"),

    ################################ User choice ###############################################

    path('user_select_choice',user.select_choice,name="choice_select"),

    ################################ User View result ##########################################

    path('user_view_result',user.view_result,name="result_user_view"),



    ##############################################################################################################################################

    ################################################################### Candidate Module ##########################################################

    ################################ search ######################################################

    path('candidate_search',candidate.search,name="can_search"),

    ################################# Candidaate Registration Page Urls ###########################

    path('candidate_registration_page<req_id>',candidate.load_candidate_registration,name="registration_page_candidate"),

    ################################# Candidate View Nomination Status Url ##########################

    path('candidate_view_nomination_status',candidate.view_nomination_status,name="view_candidate_nomination"),




    ################################################################################################################################################

    ################################ Login Page Url ###############################################

    path('',signin.display_login_page,name="login_page"),

    ################################################################################################

    ###############################################################################################################################################
    path('voteview',user.voteview,name='voteview'),
    path('niminationview',user.niminationview,name='niminationview'),
    path('complaint',user.Createcomplaint,name='complaint'),
    path('complaint_view',admin.complaint_view,name='complaint_view'),
    path('complaint_reply/<int:id>/',admin.complaint_reply,name='complaint_reply'),
    path('user_complaint_view',user.user_complaint_view,name='user_complaint_view'),
    path('PartyRegistrationView',party.PartyRegistrationView,name='PartyRegistrationView'),
    # path('userview',signin.userview,name='userview'),
    path('CreateManifestoView',party.CreateManifestoView,name='CreateManifestoView'),
    path('PARTYview_result',party.PARTYview_result,name='PARTYview_result'),
    path('phome',party.phome,name='phome'),
    path('uhome',user.uhome,name='uhome'),
]
