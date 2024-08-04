from django.db import models
from django_extensions.db.models import TimeStampedModel
from utils import abstract_models
from .modules import measure_units


class Item(
    TimeStampedModel,
    abstract_models.UserOperations,
    abstract_models.Model
    ):
    """Item master file
    """
    name = models.CharField(max_length=20, null=False, unique=True)
    description = models.TextField(null=True, blank=True)
    volume = models.FloatField(verbose_name="Volume", null=False, default=0.)
    weigth = models.FloatField(verbose_name="Weigth", null=False, default=0.)
    volume_measure = models.CharField(
        max_length=5,
        verbose_name="Volume measure unit",
        choices=measure_units.VOLUME,
        default='cm3',
        null=False,
        blank=False
    )
    weigth_measure = models.CharField(
        max_length=10,
        verbose_name="Weigth measure unit",
        choices=measure_units.WEIGTH,
        default='g',
        null=False,
        blank=False
    )
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
