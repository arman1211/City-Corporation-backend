from rest_framework import serializers
from .models import ProblemReportSolve,ServiceRequestSolve

class ProblemReportSolveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemReportSolve
        fields = ['problem', 'authority', 'description']

    def create(self, validated_data):
        problem_solve = ProblemReportSolve.objects.create(**validated_data)

        problem = validated_data['problem']
        problem.status = 'in_progress'
        problem.save()

        return problem_solve

class ProblemReportByProblemIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemReportSolve
        fields = '__all__'
    

    
class ServiceRequestSolveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequestSolve
        fields = ['service', 'authority', 'description']

    def create(self, validated_data):
        service_solve = ServiceRequestSolve.objects.create(**validated_data)

        service = validated_data['service']
        service.status = 'in_progress'
        service.save()

        return service_solve
    
class ServiceRequestByServiceIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequestSolve
        fields = '__all__'