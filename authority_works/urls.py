from django.urls import path
from .views import ProblemReportSolveView,ServiceRequestSolveView,ServiceRequestByServiceIdView,ProblemReportByProblemIdView

urlpatterns = [
    path('problem-report/solve/', ProblemReportSolveView.as_view(), name='problem-report-solve'),
    path('problem-report/solve/<int:problem_id>', ProblemReportByProblemIdView.as_view(), name='problem-report-solve-byId'),
    path('service-request/solve/', ServiceRequestSolveView.as_view(), name='service-request-solve'),
    path('service-request/solve/<int:service_id>', ServiceRequestByServiceIdView.as_view(), name='service-request-solve-byId'),
]