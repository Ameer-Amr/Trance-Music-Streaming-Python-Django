from django.urls import path
from.import views


urlpatterns = [

    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('upload_song', views.upload_song, name='upload_song'),
    path('song_list', views.song_list, name='song_list'),
    path('edit_song/<int:song_id>/',views.edit_song,name='edit_song'),
    path('delete_song/<int:song_id>/',views.delete_song,name='delete_song')


]