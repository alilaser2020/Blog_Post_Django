from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post


class HomeView(ListView):
    """
    A class view for home page of site
    """
    model = Post
    template_name = 'home.html'


class NewPostView(CreateView):
    """
    A class view for add post from frontend (Create of CRUD operations)
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    template_name = 'new_post.html'


class DetailPostView(DetailView):
    """
    A class view for reading details of post (Read of CRUD operations)
    """
    model = Post
    template_name = 'single_post.html'
