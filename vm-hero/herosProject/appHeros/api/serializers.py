from rest_framework import serializers
from appHeros import models

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '_all_'

class CharacterSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Character
        fields = '_all_'

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '_all_'