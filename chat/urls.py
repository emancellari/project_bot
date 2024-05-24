from django.urls import path
from .views import chatbot_view, upload_csv_view

urlpatterns = [
    path('', chatbot_view, name='chatbot'),
    path('upload_csv/', upload_csv_view, name='upload_csv'),
]
