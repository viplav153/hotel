from django.urls import path,include
from django.contrib.auth import views as auth_views
from .import views


urlpatterns=[
path('signup_customer',views.signup_customer,name='signup_customer'),
path('signup_hotel',views.signup_hotel,name='signup_hotel'),
path('login_hotel',views.login_hotel,name='login_hotel'),
path('login_customer',views.login_customer,name='login_customer'),
path('logout',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
path('profile',views.profile,name='profile'),
path('profile_view',views.profile_view,name='profile_view'),

path('change_password',views.change_password,name='change_password')



]