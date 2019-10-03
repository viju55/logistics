from django.urls import path
from .import views

urlpatterns = [
    path("", views.base, name="base"),
    # path('<str:category_slug>', views.product_list, name="product_list_by_category"),
    # path('<int:id>/<str:slug>/', views.product_detail, name="product_detail"),
    # path('about/', views.About, name='about'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('air/', views.air, name='air'),
    path('ocean/', views.ocean, name='ocean'),
    path('ground/', views.ground, name='ground'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='user_logout'),
    path('userhome', views.userhome, name='userhome'),
    path('air1/', views.air1, name='air1'),
    path('ocean1/', views.ocean1, name='ocean1'),
    path('groundfright/', views.groundfright, name='groundfright'),
    path('BOOK/', views.BOOK, name='BOOK'),

]
