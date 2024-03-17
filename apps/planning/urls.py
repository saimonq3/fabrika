from django.urls import path

from apps.planning.views import DaysView, HoursView, UserSchedule

urlpatterns = [
	path('get-days/<int:year>/<int:month>/', DaysView.as_view()),
	path('hours/<int:year>/<int:month>/<int:day>/', HoursView.as_view()),
	path('user-hours', UserSchedule.as_view()),
]