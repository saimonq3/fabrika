from django.urls import path

from apps.planning.views import DaysView, HoursView

urlpatterns = [
	path('get-days/<int:year>/<int:month>/', DaysView.as_view()),
	path('hours/<int:year>/<int:month>/<int:day>/', HoursView.as_view()),
]