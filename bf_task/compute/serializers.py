from rest_framework import serializers

from bf_task.compute.models import UserCSVProvidedFile, ComputedCSVCalculation


class CSVFileUploadViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCSVProvidedFile
        fields = "__all__"

    def create(self, validated_data):
        return UserCSVProvidedFile.objects.create(**validated_data)


class ComputedCSVCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputedCSVCalculation
        fields = "__all__"