import calendar
import datetime

from django.db import transaction
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from apps.planning.models import RentHours, Schedule, Tenantry
from apps.planning.tasks import telegram_notify
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
		hours = [i for i in range(int(settings.TIME_START), int(settings.TIME_STOP) + 1)]

		for hour in rent_hours:
			if hour.time.hour in hours:
				hours.remove(hour.time.hour)

		return Response(hours)

	@transaction.atomic
	def post(self, request, year=None, month=None, day=None):
		list_hours = request.data.get('hours')
		for try_hour in list_hours:
			if try_hour not in self.get(request, year, month, day).data:
				return Response(status=HTTP_400_BAD_REQUEST)
		try:
			tenantry = Tenantry.objects.get(name=request.data.get('name'), phone=request.data.get('phone'))
		except Tenantry.DoesNotExist:
			tenantry = Tenantry.objects.create(name=request.data.get('name'), phone=request.data.get('phone'))
		rent_hours = []
		for hour in list_hours:
			rent_hours.append(RentHours.objects.create(
				day=datetime.date(year, month, day),
				time=datetime.time(hour=hour, minute=0, second=0),
			))
		schedule = Schedule.objects.create(tenantry=tenantry)
		schedule.schedule_hours.set(rent_hours)

		pre_hours = [f'{i.day.strftime("%d.%m.%y")} => {i.time.hour}:00 - {i.time.hour + 1}:00' for i in schedule.schedule_hours.all()]  # noqa: E501
		hours = '\n'
		for hour in pre_hours:
			hours += hour + '\n'

		telegram_notify.delay(
			{
				'name': schedule.tenantry.name,
				'phone': schedule.tenantry.phone,
				'hours': hours

			}
		)
		return Response()
