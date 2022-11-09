from .import views
from django.urls import path,include



urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.registerpage, name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logout,name='logout'),
    path('otp/<cust_uid>/',views.otp,name='otp'),
    path('search/<cust_uid>/',views.search,name='search'),
    path('domestic/',views.domestic,name='domestic'),
    path('location/<cust_uid>/',views.location,name='location'),
    path('wlog/',views.workerlogin,name='wlog'),
    path('wreg/',views.wreg,name='wreg'),
    path('wotp/<uid>/',views.wotp,name='wotp'),
    path('application_form/<cust_uid>/<uid>/',views.application,name='application_form'),
    path('schedule/<uid>/',views.schedule,name='schedule'),
    path('dashboard/<cust_uid>/',views.dashboard,name='dashboard'),

]