from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import Room, Comment
from .forms import CommentForm


class RoomListView(generic.ListView):
    model = Room
    template_name = 'rooms/room_list.html'


class RoomDetailView (generic.DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'

    def add_comment(request, pk):
        comment = Comment()
        comment.text = request.POST['text']
        comment.room_id = pk
        comment.save()
        return HttpResponseRedirect(reverse('rooms:detail', args=(pk,)))


# class UserRoomView(generic.Listview):
#     model = Room
#     template_name = 'rooms/user_room_list.html'
#
#     def add_room(request, pk):
#         room = Room()
#         room.name = pk


# def add_comment(self, pk):
#     import pdb; pdb.set_trace()
#
#     return HttpResponseRedirect(reverse('rooms:detail', args=(pk,)))




# class CommentCreateView(generic.CreateView):
#     model = Comment
#     template_name = 'rooms/comment_form.html'
#     fields = '__all__'
#
#     def form_valid(self):
#         import pdb; pdb.set_trace()
