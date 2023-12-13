from django.urls import path
from vendor import views

app_name = "vendor"

urlpatterns = [
    path("vendorsearch", views.AXvenderSearch, name="AXvenderSearch"),
    path("pending", views.pending, name="pending"),
    path("reviewing", views.reviewing, name="reviewing"),
    path("creating", views.createRequest, name="createRequest"),
    path('set_request/<int:deal_number>/<str:vendor_name>/', views.setRequest, name="setRequest"),
    path('review_request/<int:deal_number>/<str:vendor_name>/', views.reviewRequest, name="reviewRequest"),
    path('uploadexcel', views.upload_excel, name='upload_excel'),
    path('licensemanagement', views.licensemanagement, name='licensemanagement'),

]