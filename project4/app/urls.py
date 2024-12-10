from django.urls import path
from.import views
urlpatterns = [
    path('',views.register),
    path('',views.userome),
    # path('login',views.index2),
    # path('home',views.home),
    # path('admlogin',views.adminlogin),
    # path('adminhome',views.adminhome),
    
]