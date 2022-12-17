from django.urls import path
from .views import Landing

urlpatterns = [path("", Landing.as_view(), name="landing")]
