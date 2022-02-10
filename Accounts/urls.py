from django.urls import path
from.import views


urlpatterns = [

    path('user_login/', views.user_login, name='user_login'),
    path('user_register', views.user_register, name='user_register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout', views.logout, name='logout'),
    path('user_profile',views.user_profile, name='user_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    
    

]