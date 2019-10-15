from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Room, Comment
from .forms import CommentForm


class RoomListView(generic.ListView):
    model = Room
    template_name = 'rooms/room_list.html'

class RoomDetailView (generic.DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'

class CommentCreateView(generic.CreateView):
    model = Comment
    success_url = reverse_lazy('rooms:detail')
    fields = '__all__'
    

    def form_valid(self, form):
        import pdb; pdb.set_trace()
        return super().form_valid(form)
