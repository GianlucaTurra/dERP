"""
Module for classes to import in models definitio to keep it DRY
"""

import uuid
from django.db import models
from django.contrib.auth.models import User


class Model(models.Model):
    """Utility class for uuid
    This only inherit the django Model class to chango the
    default id with the uuid
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        """
        Defines the model as an abstract class
        """

        abstract = True


class UserOperations(models.Model):
    """
    Utility class to add fields related to users working on the records
    """

    created_by = models.ForeignKey(
        User, related_name="+", on_delete=models.CASCADE, null=True
    )
    last_modified_by = models.ForeignKey(
        User, related_name="+", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        """
        Defines the model as an abstract class
        """

        abstract = True
