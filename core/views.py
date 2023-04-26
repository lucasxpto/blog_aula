from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, FormView

from core.forms import EmailForm
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


class FormContatoView(FormView):
    template_name = 'blog/post/enviarpost.html'
    form_class = EmailForm
    success_url = reverse_lazy('listar_posts')

    def get_post(self, id_post):
        try:
            return Post.publicados.get(pk=id_post)
        except Post.DoesNotExist:
            messages.error(self.request, 'Post não encontrado!')
            reverse_lazy('listar_posts')

    def get_context_data(self, **kwargs):
        context = super(FormContatoView, self).get_context_data(**kwargs)
        context['post'] = self.get_post(self.kwargs['pk'])
        return context

    def form_valid(self, form):
        meupost = self.get_context_data()['post']
        form.enviar_email(meupost)
        messages.success(self.request, f'Post {meupost.titulo} '
                                       f'enviado com sucesso.')
        return super(FormContatoView, self).form_valid(form)

    def form_invalid(self, form):
        meupost = self.get_context_data()['post']
        messages.error(self.request, f'Post {meupost.titulo} não enviado.')
        return super(FormContatoView, self).form_invalid(form)
