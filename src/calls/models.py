from django.conf import settings
from django.db import models

from services.models import Service





User = settings.AUTH_USER_MODEL

class Call(models.Model):
  date                = models.DateTimeField(auto_now_add=True)
  user                = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
  services            = models.ManyToManyField(Service, blank=True)
  account             = models.CharField(max_length=200, blank=True, null=True)
  mcDispatchNumber    = models.CharField(max_length=200, blank=True, null=True)
  mcMembershipNumber  = models.CharField(max_length=200, blank=True, null=True)
  PoNumber            = models.CharField(max_length=200, blank=True, null=True)
  mcCoverageAmount    = models.CharField(max_length=200, blank=True, null=True)
  customerName        = models.CharField(max_length=200, blank=True, null=True)
  customerPhone       = models.CharField(max_length=200, blank=True, null=True)
  customerEmail       = models.EmailField(max_length=200, blank=True, null=True)
  customerAddress     = models.CharField(max_length=200, blank=True, null=True)
  pickupLocation      = models.CharField(max_length=200, blank=True, null=True)
  dropLocation        = models.CharField(max_length=200, blank=True, null=True)
  milesToVeh          = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
  milesTowed          = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
  reason              = models.CharField(max_length=200, blank=True, null=True)
  invoiceNumber       = models.CharField(max_length=200, blank=True, null=True)
  vehLicence          = models.CharField(max_length=200, blank=True, null=True)
  vehLicenceState     = models.CharField(max_length=200, blank=True, null=True)
  vehVin              = models.CharField(max_length=200, blank=True, null=True)
  vehYear             = models.CharField(max_length=200, blank=True, null=True)
  vehMake             = models.CharField(max_length=200, blank=True, null=True)
  vehModel            = models.CharField(max_length=200, blank=True, null=True)
  vehColor            = models.CharField(max_length=200, blank=True, null=True)
  vehOdom             = models.CharField(max_length=200, blank=True, null=True)
  notes               = models.CharField(max_length=200, blank=True, null=True)
  billingNotes        = models.CharField(max_length=200, blank=True, null=True)
  is_active           = models.BooleanField(default=True)
  is_paid             = models.BooleanField(default=False)
  is_audited          = models.BooleanField(default=False)
  driver              = models.CharField(max_length=200, blank=True, null=True)
  truck               = models.CharField(max_length=200, blank=True, null=True)
  total               =  models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  re                = models.DateTimeField(auto_now_add=False, blank=True, null=True)
  di                = models.DateTimeField(auto_now_add=False, blank=True, null=True)
  er                = models.DateTimeField(auto_now_add=False, blank=True, null=True)
  ol                = models.DateTimeField(auto_now_add=False, blank=True, null=True)
  cl                = models.DateTimeField(auto_now_add=False, blank=True, null=True)

  def __str__(self):
    return self.requestedBy



class Cart(models.Model):
  user      = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
  services  = models.ManyToManyField(Service, blank=True)
  total     =  models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  updated   = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.id)
