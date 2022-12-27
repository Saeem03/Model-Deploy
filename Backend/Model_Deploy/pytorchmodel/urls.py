from django.urls import path,include
from pytorchmodel import views
urlpatterns = [
    path('',views.snippet_list),
    path('complaint_submission',views.complaint_submission),
    path('feedback_submission',views.feedback_submission),
]
