from django.shortcuts import render

from django.http import HttpResponse
from .models import Friend
# Create your views here.
from django.views.generic import ListView,DetailView

class FriendList(ListView):
    model =Friend
    
class FriendDetail(DetailView):
    model =Friend
