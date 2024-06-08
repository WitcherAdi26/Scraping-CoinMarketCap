from rest_framework import serializers

class StartScrapingSerializer(serializers.Serializer):
    payload=serializers.ListField(
        child=serializers.CharField(max_length=30)
    )