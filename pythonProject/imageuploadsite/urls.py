
from django.urls import path
from uploader import views

urlpatterns = [
    path('', views.upload_page, name='upload'),
]
