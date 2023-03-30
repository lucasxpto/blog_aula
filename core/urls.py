from django.urls import path
from .views import ListarPostsListView

urlpatterns = [
    path('', ListarPostsListView.as_view(), name='home'),
]