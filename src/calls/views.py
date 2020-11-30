from django.shortcuts import render

# Create your views here.
def cart_home(request):
    return render(request, "calls/call_list.html", {})