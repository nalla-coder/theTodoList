from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Post

class HomeView(ListView):
    model  = Post
    template_name = 'home.html'

class PostViewDetails(DetailView):
    model = Post
    template_name = "post.html"

class Create(CreateView):
    model = Post
    template_name = "create.html"
   

