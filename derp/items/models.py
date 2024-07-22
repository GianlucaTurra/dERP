from django.db import models
from django_extensions.db.models import TimeStampedModel
from utils import abstract_models


class Item(
    TimeStampedModel,
    abstract_models.UserOperations,
    abstract_models.Model
    ):
    """Item master file
    """
    name = models.CharField(max_length=20, null=False, unique=True)
    description = models.TextField(null=True, blank=True)
    volume_cm3 = models.FloatField(verbose_name="Volume in cm3", null=False, default=0.)
    weigth_g = models.FloatField(verbose_name="Weigth in grams", null=False, default=0.)
    components = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        """Model meta information for db
        """
        verbose_name_plural = 'Items'
        db_table = 'items'
        db_table_comment = 'Items basic informations'
        get_latest_by = '-modified'
        ordering = ['name']

    def __str__(self) -> str:  # pylint: disable=E0307
        return self.name
