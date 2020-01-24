from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('resident_api',views.resident_list),
    path('federal_api',views.federal_list),
    path('visitor_api',views.visitor_list),
    path('notice',views.notice),


]