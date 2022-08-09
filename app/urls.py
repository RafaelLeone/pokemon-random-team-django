from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import forms


urlpatterns = [
    # LOGIN
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="app/login.html",
            authentication_form=forms.LoginForm,
        ),
        name="app.login",
    ),
    path("cadastrar/", views.UsuarioCreate.as_view(), name="app.cadastrar"),
    path("logout/", auth_views.LogoutView.as_view(), name='app.logout'),
    path('', views.app_index, name="app.index"),
]
