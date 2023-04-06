from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from core.models import Post


class IndexView(TemplateView):
    template_name = "blog/index.html"

class ListarPostsListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post/listarposts.html'
    queryset = Post.publicados.all()
    paginate_by = 2


class DetalhePostView(DetailView):
    template_name = "blog/post/detalhepost.html"
    context_object_name = 'post'
    queryset = Post.publicados.all()
