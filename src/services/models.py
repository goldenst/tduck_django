from django.db import models

class Service(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  description = models.CharField(max_length=200, blank=True, null=True)
  rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

  def __str__(self):
    return self.name