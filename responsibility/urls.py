from django.urls import path
from responsibility import views

app_name = "responsibility"

urlpatterns = [
    path("", views.responsibilityview, name="responsibility"),
]