from django.urls import path
from .views import ProblemReportView,ProblemReportListViewSet,ServiceRequestListViewSet, ServiceRequestView, ProblemTypeListView,ServiceTypeListView,ProblemTypeDetailsView,ProblemTypeUpdateView,ProblemTypeDeleteView,ProblemTypeCreateView,ServiceTypeCreateView,ServiceTypeDeleteView,ServiceTypeDetailsView,ServiceTypeUpdateView,ProblemReportListByCitizenView,ServiceRequestListByCitizenView

urlpatterns = [
    path('report-problem/', ProblemReportView.as_view(), name='report-problem'),
    path('report-problem/list', ProblemReportListViewSet.as_view(), name='report-problem-list'),
    path('report-problem/citizen/<int:citizen_id>', ProblemReportListByCitizenView.as_view(), name='report-problem-citizen'),
    path('request-service/list', ServiceRequestListViewSet.as_view(), name='request-service-list'),
    path('request-service/', ServiceRequestView.as_view(), name='request-service'),
    path('request-service/citizen/<int:citizen_id>', ServiceRequestListByCitizenView.as_view(), name='request-service-citizen'),
    path('problem-type/list/', ProblemTypeListView.as_view(), name='problem-type'),
    path('problem-type/create/', ProblemTypeCreateView.as_view(), name='problem-type-create'),
    path('problem-type/details/<int:pk>/', ProblemTypeDetailsView.as_view(), name='problem-type-details'),
    path('problem-type/update/<int:pk>/', ProblemTypeUpdateView.as_view(), name='problem-type-update'),
    path('problem-type/delete/<int:pk>/', ProblemTypeDeleteView.as_view(), name='problem-type-delete'),
    path('service-type/list/', ServiceTypeListView.as_view(), name='service-type'),
    path('service-type/create/', ServiceTypeCreateView.as_view(), name='service-type-create'),
    path('service-type/details/<int:pk>/', ServiceTypeDetailsView.as_view(), name='service-type-details'),
    path('service-type/update/<int:pk>/', ServiceTypeUpdateView.as_view(), name='service-type-update'),
    path('service-type/delete/<int:pk>/', ServiceTypeDeleteView.as_view(), name='service-type-delete'),
]