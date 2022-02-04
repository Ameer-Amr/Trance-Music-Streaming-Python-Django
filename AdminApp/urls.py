from django.urls import path
from.import views


urlpatterns = [

    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('upload_song', views.upload_song, name='upload_song'),
    path('song_list', views.song_list, name='song_list'),

]