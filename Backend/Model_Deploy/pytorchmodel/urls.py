from django.urls import path,include
from pytorchmodel import views
urlpatterns = [
    path('complaint_submission',views.complaint_submission),
    path('feedback_submission',views.feedback_submission),
]
