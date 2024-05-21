# Imports
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from DjangoProject import settings

# URL Patterns
urlpatterns= [
    path("", views.home, name ="shop-page"),
    path("register/", views.register, name ="register-page"),
    path("login/", LoginView.as_view(template_name="shop/login.html"),name="login-page"),
    path("logout/", LogoutView.as_view(), {"next_page": settings.LOGOUT_REDIRECT_URL}, name="logout-page"),
]

def signup(request):
    pass