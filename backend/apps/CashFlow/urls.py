from django.urls import path
from .views import SendPromptAPIView

urlpatterns = [
    path('send/', SendPromptAPIView.as_view()),
]
