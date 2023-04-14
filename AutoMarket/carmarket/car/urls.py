from django.urls import path
from . import views
from django.conf.urls.static import static, settings # для картинок


urlpatterns = [
    path('', views.index, name='index'),
    path('car_list', views.car_list, name='car_list'),
    path('contacts', views.contacts, name='contacts'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='car-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)