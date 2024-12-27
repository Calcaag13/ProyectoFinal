from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'Pagina/lista_posteos.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'Pagina/detalle_posteos.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Pagina/posteo_forms.html'
    success_url = reverse_lazy('Pagina:post_list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'Pagina/posteo_forms.html'
    success_url = reverse_lazy('Pagina:post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'Pagina/eliminar_posteo.html'
    success_url = reverse_lazy('Pagina:post_list')


def about_view(request):
    return render(request, 'Pagina/about.html')

