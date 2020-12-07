
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CallCreateForm
from .models import Call

# Create your views here.
# def cart_home(request):
#     return render(request, "calls/call_list.html", {})

class CallListView(ListView):
    queryset = Call.objects.all()

class CallDetailView(DetailView):
    queryset = Call.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CallDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context 

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Call.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Call Does Not exist')
        return instance


class CallCreateView(CreateView):
    # queryset = Call.objects.all()
    form_class = CallCreateForm
    template_name = 'calls/create_call.html'
    success_url = '/calls'

    def form_invalid(self, form):
        print(ValueError)
        

    def form_valid(self, form):
        return super().form_valid(form)
    
   