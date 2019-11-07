from rest_framework import serializers


class MeSerializer(serializers.Serializer):
    is_partner_engineer = serializers.BooleanField()
