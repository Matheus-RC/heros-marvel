from rest_framework import viewsets
from appHeros.api import serializers
from appHeros import models
from .api_request import carregar_Charactere

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializers
    querySet = models.Group.objects.all()
    carregar_Charactere(None)


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CharacterSerializers
    querySet = models.Character.objects.all()
