from . import views
from django.urls import path,include



urlpatterns = [
    path('hom/', views.home, name='home'),
    path('register/',views.registerpage, name='register'),
    path('login/',views.loginpage,name='login'),
    path('otp/<uid>/',views.otp,name='otp'),
    path('search/',views.search,name='search'),
    path('domestic/',views.domestic,name='domestic'),
    path('location/',views.location,name='location'),

]