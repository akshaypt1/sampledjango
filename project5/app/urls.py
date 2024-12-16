from django.urls import path
from.import views
urlpatterns = [
    path('',views.register),
    path('uslogin',views.userlogin),
    path('',views.userhome),
    path('',views.adminlogin),
    path('',views.adminhome),
    path('userlogout',views.logout),

    
]