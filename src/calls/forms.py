from django import forms
from django.contrib.auth import  get_user_model

User = get_user_model()

from .models import Call

class CallCreateForm(forms.ModelForm):
    class Meta:
        model = Call 
        fields = ( 'user','services',            
  'account',             
  'mcDispatchNumber',    
  'mcMembershipNumber',  
  'PoNumber',
  'mcCoverageAmount',    
  'customerName',   
  'customerPhone',       
  'customerEmail',      
  'customerAddress',     
  'pickupLocation',     
  'dropLocation',     
  'milesToVeh',       
  'milesTowed',         
  'reason',         
  'invoiceNumber',       
  'vehLicence',      
  'vehLicenceState',     
  'vehVin',    
  'vehYear',             
  'vehMake',            
  'vehModel',            
  'vehColor',           
  'vehOdom',           
  'notes',            
  'billingNotes',        
  'is_active',      
  'is_paid',          
  'is_audited',         
  'driver',         
  'truck',             
  'total',            
  're',            
  'di',               
  'er',              
  'ol',               
 'cl',)   

               

#   services    = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Service Requested'
#              }))         
#   account      = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Requested By'
#              }))        
#   mcDispatchNumber  = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Dispatch / Call number'
#              }))   
#   mcMembershipNumber   = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Membership number'
#              }))
#   PoNumber     = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'PO Number'
#              }))        
#   mcCoverageAmount     = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Coverage Limit'
#              }))
#   customerName     = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Customer Full Name'
#              }))    
#   customerPhone        = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Customer Phone'
#              }))
#   customerEmail        = forms.EmailField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Customer Email'
#              }))
#   customerAddress    = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Customer Address'
#              }))  
#   pickupLocation    = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Pick up Location'
#              }))   
#   dropLocation      = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Tow Destination'
#              }))   
#   milesToVeh         = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Miles To Vehicle'
#              }))  
#   milesTowed     = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Miles Towed'
#              }))      
#   reason        = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Reason'
#              }))       
#   invoiceNumber  = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Cash Tag Number'
#              }))      
#   vehLicence    = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Licence'
#              }))       
#   vehLicenceState      = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Licence State'
#              }))
#   vehVin     = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Vin number'
#              }))          
#   vehYear             = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Year'
#              })) 
#   vehMake       = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Make'
#              }))       
#   vehModel             = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Model'
#              }))
#   vehColor         = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Color'
#              }))    
#   vehOdom              = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Odom'
#              }))
#   notes       = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Notes'
#              }))         
#   billingNotes         = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Internal Notes'
#              }))
#   is_active        = forms.BooleanField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Active'
#              }))    
#   is_paid       = forms.BooleanField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Paid'
#              }))       
#   is_audited          = forms.BooleanField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'audited'
#              })) 
#   driver      = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Driver'
#              }))         
#   truck        = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Truck'
#              }))        
#   total       = forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Total'
#              }))         
#   re              = forms.TimeField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Recieved'
#              }))   
#   di            = forms.TimeField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Dispatched'
#              }))     
#   er           = forms.TimeField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'in Route'
#              }))      
#   ol          = forms.TimeField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'On Location'
#              }))       
#   cl            = forms.TimeField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Cleared'
#              })) 


    