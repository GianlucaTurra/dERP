# pylint: disable=missing-module-docstring,invalid-str-returned
from django.db import models
from django_extensions.db.models import TimeStampedModel
from utils import abstract_models


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
