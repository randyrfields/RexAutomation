from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('call-script/', views.CallScriptView, name='call_script')
]
