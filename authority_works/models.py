from django.db import models
from service.models import ProblemReport,User,ServiceRequest

# Create your models here.

class ProblemReportSolve(models.Model):
    problem = models.ForeignKey(ProblemReport,on_delete=models.CASCADE)
    authority = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    solved_at = models.DateTimeField(auto_now_add=True)

class ServiceRequestSolve(models.Model):
    service = models.ForeignKey(ServiceRequest,on_delete=models.CASCADE)
    authority = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    solved_at = models.DateTimeField(auto_now_add=True)