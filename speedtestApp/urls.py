from django.urls import path
from . import views

urlpatterns = [
    path('', views.speed_test_view, name='speedtest'),
]
