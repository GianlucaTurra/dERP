from django.urls import path
from django.contrib.auth.views import LoginView

from core import views
from core.forms import LoginForm


app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "login/",
        LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("logout/", views.logout_user, name="logout"),
    path("menu/", views.menu, name="menu"),
]
