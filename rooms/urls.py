from django.urls import path

from . import views


app_name = 'rooms'

urlpatterns = [
    path('rooms/new', views.NewRoomView.as_view(), name='create_room'),
    path('<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='create_comment'),
    path('user/rooms/', views.UserRoomView.as_view(), name='user_rooms'),
    path('<int:pk>/user/addrooms/', views.add_room, name='user_add_rooms'),
    path('<int:pk>/', views.RoomDetailView.as_view(), name='detail'),
    path('', views.RoomListView.as_view(), name='list'),
]
