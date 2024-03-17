from django.db import models


class Photo(models.Model):
	image = models.ImageField(upload_to='images')
	description = models.TextField()
	show = models.BooleanField(default=True)

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'
