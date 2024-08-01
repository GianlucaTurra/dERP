from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .modules.apps import installed_apps


def index(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    """
    Home page's view
    """
    if not request.user.is_authenticated:
        return redirect('/login/')  
    # TODO: insert index data
    return render(request, 'core/index.html')


@login_required
def logout_user(request: HttpRequest):
    """Custom view for logout
    """
    logout(request)
    return index(request)


@login_required
def menu(request: HttpRequest) -> HttpResponse:
    """Retrieve all installed apps
    App names are displayed in a dropdown menu
    Each apps shows the links to single pages (Items -> Master file)
    """
    if request.method == 'GET':
        return render(request, 'core/menu.html', {'apps': installed_apps})
    return render(request, 'core/index.html')
