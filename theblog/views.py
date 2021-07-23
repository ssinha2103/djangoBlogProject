from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
# Create your views here.
from .models import *


def home(request):
    return render(request, 'posts/home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'posts/article_details.html'
    # success_url = reverse_lazy('home')


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    # fields = "__all__"
    success_url = reverse_lazy('home')


class AddCategoriesView(CreateView):
    model = Categories
    # form_class = PostForm
    template_name = 'posts/add_category.html'
    fields = "__all__"
    success_url = reverse_lazy('home')


class UpdatePostView(UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    form_class = EditForm
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy('home')


def category_view(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'posts/categories.html', {'cats': cats.title(), 'category_post':category_post})
