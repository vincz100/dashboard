from rest_framework.serializers import ModelSerializer

from .models import DataBase

class DataBaseSerializer(ModelSerializer):
    class Meta:
        model = DataBase
        fields = [
            'codgeo',
            'libgeo',
        ]