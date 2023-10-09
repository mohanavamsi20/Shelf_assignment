from django.db import models


class Layout(models.Model):
    data = models.JSONField()
