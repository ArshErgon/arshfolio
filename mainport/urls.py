
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('thank/', views.saving_message, name='thank'),
    path('thank-you-your-message-send/thank/you', views.thank, name='/thank/'),
]
