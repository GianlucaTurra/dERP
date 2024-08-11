# pylint: disable=no-member, missing-module-docstring
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .models import Wearhouse


@login_required
def master_file(request: HttpRequest) -> HttpResponse:
    """Get all records from the db table
    """
    wearhouses = Wearhouse.objects.all()
    return render(request, 'master_file.html', {'wearhouses': wearhouses})
