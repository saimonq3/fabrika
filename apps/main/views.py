from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.main import serializers
from apps.main.models import Photo


class PhotoView(APIView):
	permission_classes = [AllowAny, ]

	def get(self, request):
		images = Photo.objects.filter(show=True)

		serializer = serializers.PhotoSerializer(images, many=True, context={'request': request})

		return Response(serializer.data)