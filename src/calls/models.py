from django.db import models


class Call(models.Model):
  date                = models.DateTimeField(auto_now_add=True)
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
  is_paid             = models.BooleanField(default=True)
  is_audited          = models.BooleanField(default=True)
  driver              = models.CharField(max_length=200, blank=True, null=True)
  truck               = models.CharField(max_length=200, blank=True, null=True)
  re                = models.DateTimeField(auto_now_add=False)
  di                = models.DateTimeField(auto_now_add=False)
  er                = models.DateTimeField(auto_now_add=False)
  ol                = models.DateTimeField(auto_now_add=False)
  cl                = models.DateTimeField(auto_now_add=False)

  def __str__(self):
    return self.requestedBy


