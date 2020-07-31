from django.urls import path,include
from accounts import views


app_name='accounts'

urlpatterns=[
    path('',views.dashboard,name='dash'),
    path('user/',views.user_page,name='user_page'),
    path('customer/<str:pk>/',views.customers,name='customer'),
    path('products',views.products,name='products'),
    path('order/',views.create_order,name='order'),
    path('update/<str:pk>/',views.update_order,name='update_order'),
    path('delete_order/<str:pk>/',views.delete_order,name='delete'),
    path('add_product/',views.add_product,name='add_product'),
    path('update_product/<str:pk>/',views.update_product,name='update_product'),
    path('delete_product/<str:pk>/',views.delete_product,name='delete_product'),
    path('create_customer/',views.new_customers,name='new_customer'),
    path('delete_customer/<str:pk>/',views.delete_customer,name='delete_customer'),
    path('update_customer/<str:pk>/',views.update_customer,name='update_customer'),
    path('multiple_orders/<str:pk>/',views.multiple_order,name='multiple_order'),
    path('profile/',views.profile_user,name='profile_user'),



]
