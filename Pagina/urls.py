from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'Pagina'

urlpatterns = [
    path('', PostListView.as_view(), name='lista_posteos'),
    path('<int:pk>/', PostDetailView.as_view(), name='detalle_posteos'),
    path('new/', PostCreateView.as_view(), name='posteo_forms'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='posteo_forms'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='eliminar_posteo'),
]
