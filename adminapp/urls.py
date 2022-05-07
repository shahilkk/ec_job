from django.urls import path,include
from . import views

urlpatterns=[
    path('master', views.fnindex, name='index'),
    path('package', views.package, name='package'),
    path('home', views.fndash1, name='dash1'),
    path('viewwork', views.fnviewwork, name='viewwork'),
    path('viewuser', views.fnviewuser, name='viewuser'),
    path('prowork/<str:profile_id>', views.fnprowork, name='prowork'),
    path('prouser/<str:user_id>', views.fnprouser, name='prouser'),
    path('contact', views.fncontact, name='contact'),
    path('accept/<str:selected_id>', views.accpet, name='accpet'),
    path('delect/<str:delected_id>', views.delect, name='delect'),

]    