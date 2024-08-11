# pylint: disable=no-member, missing-module-docstring
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .models import Wearhouse


@login_required
def master_file(request: HttpRequest) -> HttpResponse:
    """Get all records from the db table
    """
    wearhouses = Wearhouse.objects.all()
    return render(request, 'wearhouse/master_file.html', {'wearhouses': wearhouses})


@login_required
def inline(request: HttpRequest, uuid: str) -> HttpResponse:
    """Get a single record inline for table view
    Raise 404 if no wearhouse is found
    """
    wearhouse = get_object_or_404(Wearhouse, pk=uuid)
    return render(request, 'wearhouse/inline_record.html', {'wearhouse': wearhouse})


@login_required
def delete(request: HttpRequest, uuid: str) -> HttpResponse:
    """View to delete a specific wearhouse
    GET: return the dialog to ask for deletion confirmation
    DELETE: perform the deletion and return empty html to 'remove from screen'
    Raise 404 if no wearhouse is found
    """
    wearhouse = get_object_or_404(Wearhouse, pk=uuid)
    if request.method == 'DELETE':
        wearhouse.delete()
        return render(request, 'core/empty.html')
    return render(request, 'wearhouse/confirm_delete.html', {'wearhouse': wearhouse})


@login_required
def update_inline(request: HttpRequest, uuid: str) -> HttpResponse:
    """View to update a wearhouse from the table
    GET: return the inline update 'form' with current fiel values
    POST: update the record and return the inline record
    Raise 404 if no wearhouse is found
    """
    wearhouse = get_object_or_404(Wearhouse, pk=uuid)
    if request.method == 'POST':
        wearhouse.name = request.POST['name']
        wearhouse.description = request.POST['description']
        wearhouse.address = request.POST['address']
        wearhouse.last_modified_by = request.user # type: ignore
        wearhouse.save()
        return render(request, 'wearhouse/inline_record.html', {'wearhouse': wearhouse})
    return render(request, 'wearhouse/update_inline.html', {'wearhouse': wearhouse})
