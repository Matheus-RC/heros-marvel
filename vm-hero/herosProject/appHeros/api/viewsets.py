from rest_framework import viewsets
from appHeros.api import serializers
from appHeros import models

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializers
    querySet = models.Group.objects.all()

class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CharacterSerializers
    querySet = models.Character.objects.all()

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImageSerializers
    querySet = models.Image.objects.all()
