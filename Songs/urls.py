from django.urls import path
from.import views


urlpatterns = [

    path('song_detail/<int:song_id>/', views.song_detail, name='song_detail'),

]