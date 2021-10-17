from django.db.models import fields
from rest_framework import serializers
from .models import *


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            'is_connected', 'time_refresh'
            
        )


class ClientSerializer(serializers.ModelSerializer):
    programms = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField(many=False)
    settings = SettingsSerializer(many=False, read_only=True)

    class Meta:
        model = Client
        fields = (
            'start_at', 'end_at', 'total_work', 'total_away', 'productive_time',
            'non_productive_time', 'user', 'programms', 'settings'
            )
        


