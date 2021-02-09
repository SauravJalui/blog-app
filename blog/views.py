from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    '''This view lists all the blog posts available'''
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    '''This view lists all the details in each individual posts'''
    model = Post
    template_name = 'post_detail.html'