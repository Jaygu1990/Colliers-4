from django.urls import path
from revrec import views

app_name = "revrec"

urlpatterns = [
    path('', views.revrecview, name='revrec'),
    path('tested', views.tested, name='tested'),
    path('assign/<int:deal>/', views.revrecupdate, name='revrecupdate'),
    path('test/<int:deal>/', views.testupdate, name='testupdate'),
    path('note/<int:deal>/', views.noteupdate, name='noteupdate'),
    path('uploadrevrec', views.uploadrevrec, name='uploadrevrec'),
    ]