import calendar
import datetime

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.planning.models import RentHours, Schedule, Tenantry
from limon import settings


class DaysView(APIView):
	permission_classes = [AllowAny, ]

	def get(self, request, year=None, month=None):
		num_days = calendar.monthrange(year, month)[1]
		days = [day for day in range(1, num_days + 1)]
		busy_days_list = RentHours.objects.filter(day__month=month, day__year=year).order_by('day')
		empty_days = []
		for day in days:
			if not busy_days_list.filter(day__day=day).exists():
				empty_days.append(day)
			if day_count := busy_days_list.filter(time__hour__in=settings.HOURS_WORK, day__day=day).count():
				if day_count < len(settings.HOURS_WORK):
					empty_days.append(day)
		return Response(sorted(empty_days))


class HoursView(APIView):
	permission_classes = [AllowAny, ]

	def get(self, request, year=None, month=None, day=None):
		rent_hours = RentHours.objects.filter(day__month=month, day__year=year, day__day=day)
		hours = settings.HOURS_WORK

		for hour in rent_hours:
			if hour.time.hour in hours:
				hours.remove(hour.time.hour)

		return Response(hours)

	def post(self, request, year=None, month=None, day=None):
		list_hours = request.data.get('hours')
		Tenantry.objects.create(name=request.data.get('name'), phone=request.data.get('phone'))
		for hour in list_hours:
			RentHours.objects.create(
				day=datetime.date(year, month, day),
				time=datetime.time(hour=hour, minute=0, second=0),
			)
		return Response()