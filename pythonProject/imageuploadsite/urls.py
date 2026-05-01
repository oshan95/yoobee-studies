
from django.urls import path
from uploader import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_page, name='upload'),
    path('/bmi', views.bmi_calculator, name='bmi_calculator'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
