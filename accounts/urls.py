from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('profile/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/create/', views.ProfileCreateView.as_view(), name='new_profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.SignUpView.as_view(), name='login'),
    path('', views.LogOutView.as_view(), name='logout')
]
