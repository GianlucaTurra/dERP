from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect


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
def logout_user(request: HttpRequest):
    """Custom view for logout
    Is this needed???
    """
    logout(request)
    return index(request)  # TODO: This was poorly implemented, test it and document 
