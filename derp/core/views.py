from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from .utils.apps import installed_apps


def index(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    """
    Home page's view
    """
    if not request.user.is_authenticated:
        return redirect('/login/')  # <- This might not be the way
    # TODO: insert index data
    return render(request, 'core/index.html')

# Login view is not required since the default one it's good enough here

@login_required
def logout_user(request: HttpRequest) -> HttpResponse:
    """Custom view for logout
    """
    logout(request)
    return index(request)


@login_required
def get_menu_apps(request: HttpRequest) -> HttpResponse:
    """Return the menu for all apps
    """
    return render(request, 'core/menu.html', {'apps': installed_apps})
