# pylint: disable=missing-module-docstring,invalid-str-returned
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from utils import abstract_models
from items.models import Item


class Wearhouse(
    TimeStampedModel,
    abstract_models.Model,
    abstract_models.UserOperations):
    """Basic information about a wearhouse
    AM.Model: uuid instead of simple id
    AM.UserOperation: created by and last modified by
    """
    name = models.CharField(max_length=25, null=False, blank=False, unique=True)
    description = models.TextField(null=True)
    address = models.CharField(max_length=50, null=False, blank=False)
    stockunits = models.ForeignKey(
        'wearhouse.StockUnit',
        verbose_name=_('Stock units'),
        on_delete=models.CASCADE
    )

    class Meta:
        """Meta information about the table
        """
        verbose_name_plural = 'Wearhouses'
        db_table = 'wearhouses'
        db_table_comment = 'Wearhouse basic information'
        get_latest_by = '-modified'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class StockUnit(
    TimeStampedModel,
    abstract_models.UserOperations):
    """Basic unit of a wearhouse
    Each stockunit is capable of containing a certain amount of a 
    specific item. It also carries information about the current state.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stored_quantity = models.FloatField(_('Stored quantity'), null=False)
    max_quantity = models.FloatField(_('Maximum quantity'), null=False, blank=False)

    class Meta:
        """Meta information about the table
        """
        verbose_name_plural = 'Stock units'
        db_table = 'stockunits'
        get_latest_by = '-modified'

    def __str__(self) -> str:
        return f'{self.id}: {self.stored_quantity}/{self.max_quantity}'

    def __repr__(self) -> str:
        return self.id # type: ignore
