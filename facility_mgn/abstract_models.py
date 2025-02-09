from django.db import models
# from accounts.models import Marchant, Store

class TimeStampedModel(models.Model):
    """
    Abstract base model with fields for tracking object creation and last
    update dates.
    """

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True

