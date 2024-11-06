from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.show_account,name='account'),
    path('registration-success/', views.registration_success, name='registration_success'),
]
