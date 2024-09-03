# pylint: disable=no-member, missing-module-docstring
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

from .forms import WearhouseForm
from .models import Wearhouse


EMPTY_TEMPLATE = 'core/empty.html'
WEARHOUSE_MASTER_FILE = 'wearhouse/master_file.html'
WEARHOUSE_INLINE_RECORD = 'wearhouse/inline_record.html'
WEARHOUSE_CONFIRM_DELETE = 'wearhouse/confirm_delete.html'
WEARHOUSE_UPDATE_INLINE = 'wearhouse/update_inline.html'
WEARHOUSE_ADD_WEARHOUSE = 'wearhouse/add_wearhouse.html'
WEARHOUSE_ADD_INLINE = 'wearhouse/add_wearhouse_inline.html'


@login_required
def master_file(request: HttpRequest) -> HttpResponse:
    """Get all records from the db table
    """
    wearhouses = Wearhouse.objects.all()
    return render(request, WEARHOUSE_MASTER_FILE, {'wearhouses': wearhouses})


@login_required
def inline(request: HttpRequest, uuid: str) -> HttpResponse:
    """Get a single record inline for table view
    Raise 404 if no wearhouse is found
    """
    wearhouse = get_object_or_404(Wearhouse, pk=uuid)
    return render(request, WEARHOUSE_INLINE_RECORD, {'wearhouse': wearhouse})


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
        return render(request, EMPTY_TEMPLATE)
    return render(request, WEARHOUSE_CONFIRM_DELETE, {'wearhouse': wearhouse})


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
        return render(request, WEARHOUSE_INLINE_RECORD, {'wearhouse': wearhouse})
    return render(request, WEARHOUSE_UPDATE_INLINE, {'wearhouse': wearhouse})


@login_required
def new(request: HttpRequest) -> HttpResponse:
    """View to add a new Wearhouse with a dialog form
    GET: return the empty form
    POST: save the new record and redirect to master TODO: this has to change
    TODO good place to introduce the role of user_groups
    """
    if request.method == 'POST':
        form = WearhouseForm(request.POST)
        if form.is_valid():
            wearhouse: Wearhouse = form.save()
            wearhouse.created_by = request.user # type: ignore
            wearhouse.save()
            return redirect('/wearhouse/master')
    form = WearhouseForm()
    return render(request, WEARHOUSE_ADD_WEARHOUSE, {'form': form})


@login_required
def new_inline(request: HttpRequest) -> HttpResponse:
    """View to add a new Wearhouse with the inline "form"
    GET: return the inline empty inputs
    POST: save the new record and return the inline record template
    """
    if request.method == 'POST':
        wearhouse = Wearhouse()
        wearhouse.name = request.POST['name']
        wearhouse.description = request.POST['description']
        wearhouse.address = request.POST['address']
        wearhouse.created_by = request.user # type: ignore
        wearhouse.save()
        return render(request, WEARHOUSE_INLINE_RECORD, {'wearhouse': wearhouse})
    return render(request, WEARHOUSE_ADD_INLINE)


@login_required
def assigne_stock_units(request: HttpRequest) -> HttpResponse:
    # TODO this method should check for wearhouse existence and add stockunits to it
    pass
