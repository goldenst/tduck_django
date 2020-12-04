from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


# from calls.views import cart_home
from .views import home_page, about_page, contact_page, loginView, RegisterView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', loginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('services/', include('services.urls', namespace='services')),
    path('calls/', include('calls.urls', namespace='calls')),
  
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)