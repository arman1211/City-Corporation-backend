from rest_framework import serializers
from .models import ProblemReport, ServiceRequest, ProblemType,ServiceType

class ProblemReportSerializer(serializers.ModelSerializer):
    problem_type_name = serializers.CharField(source='problem_type.name', read_only=True)
    class Meta:
        model = ProblemReport
        fields = ['id', 'citizen', 'problem_type', 'problem_type_name', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'status', 'created_at', 'updated_at', 'problem_type_name']

    def validate_citizen(self, value):
        if value.role != 'citizen':
            raise serializers.ValidationError("The selected user is not a citizen.")
        return value

class ProblemReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemReport
        fields = '__all__'
        depth = 1 

class ServiceRequestSerializer(serializers.ModelSerializer):
    service_type_name = serializers.CharField(source='service_type.name', read_only=True)
    class Meta:
        model = ServiceRequest
        fields = ['id', 'citizen', 'service_type','service_type_name', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']

    def validate_citizen(self, value):
        if value.role != 'citizen':
            raise serializers.ValidationError("The selected user is not a citizen.")
        return value

class ServiceRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        depth = 1

class ProblemTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemType
        fields = '__all__'

class ServiceTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'