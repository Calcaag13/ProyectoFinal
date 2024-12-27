from django.urls import path
from .views import register, login_view, ProfileView
from django.contrib.auth.views import LogoutView

app_name = 'Cuentas'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
