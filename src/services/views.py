from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Service

class ServiceListView(ListView):
    queryset = Service.objects.all()

class ServiceDetailView(DetailView):
    queryset = Service.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context 

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Service.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Service Does Not exist')
        return instance

