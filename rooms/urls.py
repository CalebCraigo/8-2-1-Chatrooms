from django.urls import path

from . import views


app_name = 'rooms'

urlpatterns = [
    path('<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='create'),
    path('<int:pk>/', views.RoomDetailView.as_view(), name='detail'),
    path('', views.RoomListView.as_view(), name='list'),
]
