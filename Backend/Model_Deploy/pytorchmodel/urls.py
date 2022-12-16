from django.urls import path,include
from pytorchmodel import views
urlpatterns = [
    path('',views.detail)
]
