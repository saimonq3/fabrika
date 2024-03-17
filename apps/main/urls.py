from django.urls import path

from apps.main import views

urlpatterns = [
	path('photos', views.PhotoView.as_view())
]