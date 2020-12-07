from django import forms
from django.contrib.auth import  get_user_model

User = get_user_model()

from .models import Call

class CallCreateForm(forms.ModelForm):
    class Meta:
        model = Call 
        fields =  ('user','services', 'account', 'mcDispatchNumber', 'mcMembershipNumber','PoNumber','mcCoverageAmount', 'customerName', 'customerPhone', 'customerEmail', 'customerAddress', 'pickupLocation', 'dropLocation', 'milesToVeh', 'milesTowed', 'reason', 'invoiceNumber', 'vehLicence', 'vehLicenceState', 'vehVin', 'vehYear', 'vehMake', 'vehModel', 'vehColor', 'vehOdom', 'notes', 'billingNotes', 'is_active', 'is_paid', 'is_audited', 'driver', 'truck',  'total', 're', 'di', 'er', 'ol', 'cl')
 

        # widgets = {
        #     'account' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requested By'}),
        #     'services' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Service Requested'}),
        #     'mcDispatchNumber' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Call Number'}),
        #     'mcMembershipNumber' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Membership Number'}),
        #     'poNumber' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Po Number'}),
        #     'mcCoverageAmount' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coverage Amount'}),
        #     'customerName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer'}),
        #     'customerPhone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        #     'customerEmail': forms.TextInput(attrs={'class': 'form-control'}),
        #     'customerAddress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        #     'pickupLocation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breakdown Location'}),
        #     'dropLocation' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tow Destination'}),
        #     'milesToVeh' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Miles to Vehicle'}),
        #     'milesTowed' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Miles Towed'}),
        #     'reason' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reason'}),
        #     'invoiceNumber' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'invoice Number'}),
        #     'vehLicence' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Plate'}),
        #     'vehLicenceState' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle State'}),
        #     'vehVin' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Vin'}),
        #     'vehYear' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Year'}),
        #     'vehMake' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Make'}),
        #     'vehModel' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Model'}),
        #     'vehColor' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Color'}),
        #     'vehOdom' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Odom'}),
        #     'notes' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notesl'}),
        #     'billingNotes' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Billing Notes'}),
        #     'is_active' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        #     'is_paid' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Paid'}),
        #     'is_audited' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Audited'}),
        #     'driver' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Driver'}),
        #     'total' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Truck'}),
        #     'truck' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),
        #     # 're' : forms.TimeField(),
        #     # 'di' : forms.TimeField(),
        #     # 'ol' : forms.TimeField(),
        #     # 'er' : forms.TimeField(),
        #     # 'cl' : forms.TimeField(),

        # }      

