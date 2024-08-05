# pylint: disable=no-member, missing-module-docstring
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import ItemForm
from .modules.measure_units import VOLUME, WEIGTH


@login_required
def master_file(request: HttpRequest) -> HttpResponse:
    """Get all items from db
    """
    items = Item.objects.all()
    return render(request, 'master_file.html', {'items': items})


@login_required
def inline(request: HttpRequest, uuid: str) -> HttpResponse:
    """Return single iteme line for table
    Used to undo the update inline
    """
    item = get_object_or_404(Item, pk=uuid)
    return render(request, 'item_inline.html', {'item': item})


@login_required
def item_detail(request: HttpRequest, uuid: str) -> HttpResponse:
    """Return template of single item detail
    """
    item = get_object_or_404(Item, pk=uuid)
    return render(request, 'item_detail.html', {'item': item})


@login_required
def new_item(request: HttpRequest) -> HttpResponse:
    """Add new Item
    GET: returns the template with the form
    POST: validates and saves the form, then renders the master again
    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item: Item = form.save()
            item.created_by = request.user # type: ignore
            item.save()
            return redirect('/items/master')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


@login_required
def new_item_inline(request: HttpRequest) -> HttpResponse:
    """Add new item with inline input
    Same as update_item_inline accepts both GET and POST
    With GET returns the template and with POST creates the new record
    """
    if request.method == 'POST':
        item = Item()
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.weigth = float(request.POST['weigth'])
        item.weigth_measure = request.POST['weigth_measure']
        item.volume = float(request.POST['volume'])
        item.volume_measure = request.POST['volume_measure']
        item.created_by = request.user # type: ignore
        item.save()
        return render(request, 'item_inline.html', {'item': item})
    return render(request, 'create_item_inline.html', {'w_options': WEIGTH, 'v_options': VOLUME})


@login_required
def delete_item(request: HttpRequest, uuid: str) -> HttpResponse:
    """Delete a record from Item
    If the record is not found a 404 response is risen
    If called from master file (GET) returns a confirmation dialog
    After deletion the user is redirected to item master page 
    """
    item = get_object_or_404(Item, pk=uuid)
    if request.method == 'DELETE':
        item.delete()
        return render(request, 'core/empty.html')
    return render(request, 'confirm_delete.html', {'item': item})


# TODO: here's some code repetition with the new item view, maybe abstract this?
@login_required
def update_item(request: HttpRequest, uuid: str) -> HttpResponse:
    """Update item from detail dialog
    GET: return the form with the initial of the fields
    POST: updates the record in the database and returns (dialog closing on its own)
    """
    item = get_object_or_404(Item, pk=uuid)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item: Item = form.save()
            item.last_modified_by = request.user # type: ignore
            item.save()
            return HttpResponse(status=202)
    else:
        form = ItemForm(initial={
            'name': item.name,
            'descritpion': item.description,
            'weigth': item.weigth,
            'weigth_measure': item.weigth_measure,
            'volume': item.volume,
            'volume_measure': item.volume_measure
        },
        auto_id=False)
    return render(request, 'update_item.html', {'form': form})


@login_required
def update_item_inline(request: HttpRequest, uuid: str) -> HttpResponse:
    """Update a record from Item
    If the record is not found a 404 response is rise
    If GET request the editable table row is returned for htmx swap
    If PUT request the actual update is performed
    """
    item = get_object_or_404(Item, pk=uuid)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.weigth = float(request.POST['weigth'])
        item.volume = float(request.POST['volume'])
        item.last_modified_by = request.user # type: ignore
        item.save()
        return render(request, 'item_inline.html', {'item': item})
    return render(request, 'update_item_inline.html', {'item': item})
