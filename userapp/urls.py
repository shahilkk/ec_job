from django.urls import path,include
from . import views

urlpatterns=[
    path('master', views.fnmaster, name='master'),
    path('home', views.fnhome, name='home'),
    path('profile', views.fnprofile, name='profile'),
    path('service', views.fnservice, name='service'),
    path('view/<str:selected_subcategory>', views.fnview, name='view'),
    path('registration', views.fnregistration, name='registration'),
    path('wrkpro/<str:selected_workerid>', views.fnwrkpro, name='wrkpro'),
    path('contacts', views.fncontact, name='contacts'),
    path('payment', views.fnpayment, name='payment'),
    path('singup', views.signup, name='singup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('workreg', views.workreg, name='workreg'),
    path('search_list', views.search_list, name='search_list'),
    path('booking', views.booking, name='booking'),
    path('quickbooking', views.quickbooking, name='quickbooking'),
    path('gallery', views.gallery, name='gallery'),
    path('price', views.price, name='price'),
    path('review', views.review, name='review'),
]