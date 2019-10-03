from django.urls import path
from . import views

urlpatterns = [
    #path('', views.transporter_details, name = "transporter_details"),
    path('login1/',views.login1,name='login1'),
    path('Transporterhome/',views.Transporterhome,name='Transporterhome'),
    path('Add/',views.Add,name='Add'),
    path('View/',views.View,name='View'),
    path('update/',views.update,name='update'),
    path('Transporter/register1',views.register1,name='Transporter/register1'),
    path('logout', views.logout, name='user_logout'),


]