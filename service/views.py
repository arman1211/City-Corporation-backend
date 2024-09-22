from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProblemType,ServiceType,ProblemReport,ServiceRequest
from .serializers import ServiceRequestListSerializer, ProblemReportSerializer,ProblemReportListSerializer, ServiceRequestSerializer,ProblemTypeListSerializer,ServiceTypeListSerializer

# --------problem report related view------- 
class ProblemReportView(APIView):
    def post(self, request):
        serializer = ProblemReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProblemReportListViewSet(generics.ListAPIView):
    queryset = ProblemReport.objects.all()
    serializer_class = ProblemReportListSerializer

class ProblemReportListByCitizenView(generics.ListAPIView):
    serializer_class = ProblemReportSerializer

    def get_queryset(self):
        citizen_id = self.kwargs['citizen_id']
        return ProblemReport.objects.filter(citizen__id=citizen_id)
# -----------service request related view ---------

class ServiceRequestView(APIView):
    def post(self,request):
        serializer = ServiceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceRequestListViewSet(generics.ListAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestListSerializer

class ServiceRequestListByCitizenView(generics.ListAPIView):
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        citizen_id = self.kwargs['citizen_id']
        return ServiceRequest.objects.filter(citizen__id=citizen_id)
    

# ----------problem type crud operation-------

class ProblemTypeListView(generics.ListAPIView):
    queryset = ProblemType.objects.all()
    serializer_class = ProblemTypeListSerializer

class ProblemTypeCreateView(generics.CreateAPIView):
    queryset = ProblemType.objects.all()
    serializer_class = ProblemTypeListSerializer

class ProblemTypeDetailsView(generics.RetrieveAPIView):
    queryset = ProblemType.objects.all()
    serializer_class= ProblemTypeListSerializer

class ProblemTypeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ProblemType.objects.all()
    serializer_class= ProblemTypeListSerializer

class ProblemTypeDeleteView(generics.DestroyAPIView):
    queryset = ProblemType.objects.all()
    serializer_class= ProblemTypeListSerializer

# -------------service type crud operation------------

class ServiceTypeListView(generics.ListAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeListSerializer

class ServiceTypeCreateView(generics.CreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeListSerializer

class ServiceTypeDetailsView(generics.RetrieveAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeListSerializer

class ServiceTypeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeListSerializer

class ServiceTypeDeleteView(generics.DestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeListSerializer
