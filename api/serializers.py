from rest_framework import serializers

class TextInputSerializer(serializers.Serializer):
    task_type = serializers.CharField()
    text = serializers.CharField()

class BenchmarkDatasetSerializer(serializers.Serializer):
    dataset = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )
