from django.urls import path
from .views import HomeView

app_name = "website"

urlpatterns = [
    path('website/',HomeView.as_view(),name='home')
]
