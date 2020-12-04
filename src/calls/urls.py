from django.urls import path

from .views import CallListView, CallDetailView, CallCreateView

app_name = 'calls'

urlpatterns = [
    
    path('', CallListView.as_view(),name='list'),
    path('create/', CallCreateView.as_view(),name='create'),
    path('<pk>/', CallDetailView.as_view(), name='detail'),
]