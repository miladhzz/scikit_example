from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class StandarizeSerializer(serializers.Serializer):
    sensor_1 = serializers.ListField(child=serializers.FloatField())
    sensor_2 = serializers.ListField(child=serializers.FloatField())
    sensor_3 = serializers.ListField(child=serializers.FloatField())
    def validate(self, data):
        list_lengths = {}
        for key, value in data.items():
            if not isinstance(value, list):
                raise serializers.ValidationError(f"{key} must be a list")
            list_lengths[key] = len(value)
        if len(set(list_lengths.values())) != 1:
            raise serializers.ValidationError("All lists must have the same length")
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token
