from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
# Create your views here.
from .models import *
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'posts/home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'posts/article_details.html'

    # success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


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
    return render(request, 'posts/categories.html', {'cats': cats.title(), 'category_post': category_post})


def category_list_view(request):
    cat_menu_list = Categories.objects.all()
    return render(request, 'posts/category_list.html', {'cat_menu_list': cat_menu_list})


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
