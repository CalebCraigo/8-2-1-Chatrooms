from django.urls import path

from . import views


app_name = 'rooms'

urlpatterns = [
    # path('<int:pk>/user/rooms/'), views.UserRoomView, name='user_rooms'),
    path('<int:pk>/comment/new/', views.RoomDetailView.add_comment, name='create_comment'),
    path('<int:pk>/', views.RoomDetailView.as_view(), name='detail'),
    path('', views.RoomListView.as_view(), name='list'),
]
