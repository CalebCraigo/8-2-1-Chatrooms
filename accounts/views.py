from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('rooms:list')
    template_name = 'signup.html'


class LogOutView(generic.TemplateView):
    template_name = 'registration/logout.html'


class ProfileCreateView(generic.CreateView):
    model = Profile
    template_name = 'registration/profile_create.html'
    success_url = reverse_lazy('rooms:list')
    fields = ('bio', 'location', 'avatar',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile_detail.html'
