from django.db import models


class Tenantry(models.Model):
	name = models.CharField(max_length=128, verbose_name='Имя')
	phone = models.CharField(max_length=11, verbose_name='Телефон')

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name = 'Арендатор'
		verbose_name_plural = 'Арендаторы'
		unique_together = ['name', 'phone']


class RentHours(models.Model):
	day = models.DateField()
	time = models.TimeField()


class Schedule(models.Model):
	tenantry = models.ForeignKey(Tenantry, on_delete=models.CASCADE, verbose_name='Арендатор', related_name='schedule')
	schedule_hours = models.ManyToManyField(RentHours, verbose_name='Часы аренды', related_name='hours')

	def __str__(self):
		return f'{self.tenantry.name}'

	class Meta:
		verbose_name_plural = 'Расписание'
		verbose_name = 'Расписание'
