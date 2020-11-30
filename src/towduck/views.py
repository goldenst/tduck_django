from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model,logout

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    return render(request, 'home_page.html', {})

def about_page(request):
    return render(request, 'about_page.html', {})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
       'form' : contact_form, 
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == 'POST':
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,'contact_page.html', context)
    
class loginView(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # context['form'] = LoginForm()
            return redirect('/')
        return super(loginView, self).form_invalid(form)

def logout_view(request):
    logout(request)
    return redirect('/')

# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         'form' : form
#     }
#     # print('user is loged in:', request.user.is_authenticated)
#     if form.is_valid():
#         # print(form.cleaned_data)
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             context['form'] = LoginForm()
#             return redirect('/')
#             # print('user is loged in:', request.user.is_authenticated)
#         else:
#             print('error')
            
#     return render(request,'auth/login.html', context)



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'

# User = get_user_model()

# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         'form' : form
#     }
#     if form.is_valid():
#         form.save()
        
#     return render(request,'auth/register.html', context)