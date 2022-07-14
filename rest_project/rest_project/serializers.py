from rest_framework import serializers


class StoreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=800)
    ratings = serializers.IntegerField(max_value=100, min_value=0)

