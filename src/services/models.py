from django.db import models
from django.urls import reverse


class ServiceManager(models.Manager):
  def get_by_id(self, id):
    qs = self.get_queryset().filter(id=id)
    if qs.count() == 1:
      return qs.first()
    return None


class Service(models.Model):
  name          = models.CharField(max_length=200,)
  slug          = models.SlugField(default='abc')
  description   = models.CharField(max_length=200, blank=True, null=True)
  rate          = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  

  objects = ServiceManager()

  def get_absolute_url(self):
    # return "/services/{pk}/".format(pk=self.pk)
    return reverse('services:detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.name