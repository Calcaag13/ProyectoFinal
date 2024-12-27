from django.urls import path
from .views import MessageListView, MessageDetailView, MessageCreateView

app_name = 'Mensajería'

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('new/', MessageCreateView.as_view(), name='message_create'),
]
