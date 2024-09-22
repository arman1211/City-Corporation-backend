from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import ProblemReportSolve,ServiceRequestSolve
from .serializers import ServiceRequestByServiceIdSerializer, ProblemReportByProblemIdSerializer, ProblemReportSolveSerializer,ServiceRequestSolveSerializer
from django.shortcuts import get_object_or_404

class ProblemReportSolveView(generics.CreateAPIView):
    queryset = ProblemReportSolve.objects.all()
    serializer_class = ProblemReportSolveSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Notify the citizen (optional)
        # self.notify_citizen(serializer.instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def notify_citizen(self, problem_solve):
    #     # Example: Send an email or notification to the citizen
    #     citizen_email = problem_solve.problem.citizen.email
    #     message = problem_solve.description
    #     # Logic to send email or message
    #     # send_email(citizen_email, "Problem Report Update", message)
    #     print(f"Sent message to {citizen_email}: {message}")

class ProblemReportByProblemIdView(generics.RetrieveAPIView):
    serializer_class = ProblemReportByProblemIdSerializer

    def get_object(self):
        problem_id = self.kwargs['problem_id']
        return get_object_or_404(ProblemReportSolve, problem__id=problem_id)
    

class ServiceRequestSolveView(generics.CreateAPIView):
    queryset = ServiceRequestSolve.objects.all()
    serializer_class = ServiceRequestSolveSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Notify the citizen (optional)
        # self.notify_citizen(serializer.instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def notify_citizen(self, problem_solve):
    #     # Example: Send an email or notification to the citizen
    #     citizen_email = problem_solve.problem.citizen.email
    #     message = problem_solve.description
    #     # Logic to send email or message
    #     # send_email(citizen_email, "Problem Report Update", message)
    #     print(f"Sent message to {citizen_email}: {message}")

class ServiceRequestByServiceIdView(generics.RetrieveAPIView):
    serializer_class = ServiceRequestByServiceIdSerializer

    def get_object(self):
        service_id = self.kwargs['service_id']
        return get_object_or_404(ServiceRequestSolve, service__id=service_id)