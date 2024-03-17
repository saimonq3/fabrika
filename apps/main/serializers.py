from rest_framework import serializers

from apps.main.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()

	class Meta:
		model = Photo
		fields = ['image', 'description']

	def get_image(self, obj):
		return self.context['request'].build_absolute_uri(obj.image.url)