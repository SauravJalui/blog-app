from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    '''This view lists all the blog posts available'''
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    '''This view lists all the details in each individual posts'''
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    '''This view creates a new post through the app'''
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    '''This view updates an existing post through the app'''
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')