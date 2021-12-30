from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='acc_home'),
    path('notice/', views.accNotice, name='notice'),

    path('logbook/', views.logbook, name='LogBook'),
    path('logbook/input-details/', views.inputDetails, name='accinputDetails'),
    # path('logbook/', views.LogBookCreate.as_view(), name='logBook'),
    # # path('success/', views.InfoSuccess, name='datainput')
    # re_path('accountant/logbook/inputderails/(?P<id>\d+)/$', views.InfoSuccess, name='datainput'),
]
