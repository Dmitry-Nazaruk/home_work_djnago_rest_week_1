from rest_framework import serializers

from rest_api.models import Store


class StoreSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # description = serializers.CharField(max_length=800)
    # ratings = serializers.IntegerField(max_value=100, min_value=0)

    class Meta:
        model = Store
        fields = (
            'title',
            'description',
            'ratings',
            'id',
            'owner',
            'status'
        )