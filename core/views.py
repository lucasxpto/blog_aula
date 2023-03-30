from django.shortcuts import render
from django.views.generic import ListView

from core.models import Post


class ListarPostsListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post/listarposts.html'
    queryset = Post.publicados.all()

