
from django.urls import path

from .views import ServiceListView, ServiceDetailView

app_name = 'services'

urlpatterns = [
    
    path('', ServiceListView.as_view(),name='list'),
    path('<pk>/', ServiceDetailView.as_view(), name='detail'),
]