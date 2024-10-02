from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import ProblemReportSolve,ServiceRequestSolve
from .serializers import ServiceRequestByServiceIdSerializer, ProblemReportByProblemIdSerializer, ProblemReportSolveSerializer,ServiceRequestSolveSerializer
from django.shortcuts import get_object_or_404
from City_corporation_backend.permissions import IsAuthority, IsCitizen

class ProblemReportSolveView(generics.CreateAPIView):
    queryset = ProblemReportSolve.objects.all()
    serializer_class = ProblemReportSolveSerializer
    permission_classes = [IsAuthority]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)


        return Response(serializer.data, status=status.HTTP_201_CREATED)

   

class ProblemReportByProblemIdView(generics.RetrieveAPIView):
    serializer_class = ProblemReportByProblemIdSerializer

    def get_object(self):
        problem_id = self.kwargs['problem_id']
        return get_object_or_404(ProblemReportSolve, problem__id=problem_id)
    

class ServiceRequestSolveView(generics.CreateAPIView):
    queryset = ServiceRequestSolve.objects.all()
    serializer_class = ServiceRequestSolveSerializer
    permission_classes = [IsAuthority]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)


        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ServiceRequestByServiceIdView(generics.RetrieveAPIView):
    serializer_class = ServiceRequestByServiceIdSerializer

    def get_object(self):
        service_id = self.kwargs['service_id']
        return get_object_or_404(ServiceRequestSolve, service__id=service_id)