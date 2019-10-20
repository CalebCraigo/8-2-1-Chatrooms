from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect


from .models import Profile
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:new_profile')
    template_name = 'signup.html'

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


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

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
