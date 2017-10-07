# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Position(models.Model):
    """
    A snapshot of the position of the accelerometer at a moment in time.
    """
    timestamp = models.DateTimeField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-timestamp",)

    def __unicode__(self):
        return str(self.timestamp)
