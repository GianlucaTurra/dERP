# pylint: disable=no-member, missing-module-docstring
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm


@login_required
def master_file(request: HttpRequest) -> HttpResponse:
    """Get all items from db
    """
    items = Item.objects.all()
    return render(request, 'master_file.html', {'items': items})

@login_required
def new_item(request: HttpRequest) -> HttpResponse:
    """Add new Item
    GET: returns the template with the form
    POST: validates and saves the form, then renders the master again
    TODO: should it really return to master? 
    """
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            item: Item = form.save()
            item.created_by = request.user
            item.save()
            return redirect('/items/master')
    else:
        form = NewItemForm()
    return render(request, 'add_item.html', {'form': form})


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
        return master_file(request)
    return render(request, 'confirm_delete.html', {'item': item})
