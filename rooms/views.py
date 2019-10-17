from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import Room, Comment
from .forms import NewRoomForm


class RoomListView(generic.ListView):
    model = Room
    template_name = 'rooms/room_list.html'


class RoomDetailView (generic.DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'


class NewRoomView(generic.CreateView):
    form_class = NewRoomForm
    template_name = 'rooms/create_room.html'


class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.room_id = self.kwargs['pk']
        return super().form_valid(form)


class UserRoomView(generic.ListView):
    model = Room
    template_name = 'rooms/user_room_list.html'
    fields = '__all__'
    def get_queryset(self):
        return Room.objects.filter(users=self.request.user)


def add_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.users.add(request.user)
    room.save()

    return HttpResponseRedirect(reverse_lazy('rooms:user_rooms'))
