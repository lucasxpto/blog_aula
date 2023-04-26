from django.urls import path
from .views import ListarPostsListView, IndexView, DetalhePostView, FormContatoView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('listar/', ListarPostsListView.as_view(), name='listar_posts'),
    path('detalhe/<int:ano>/<int:mes>/<int:dia>/<slug:slug>',
         DetalhePostView.as_view(), name='detalhe_post'),
    path('enviarpost/<int:pk>/',
         FormContatoView.as_view(),
         name='enviar_post'),
]