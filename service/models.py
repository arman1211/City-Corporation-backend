from django.db import models
from user_authentication.models import User
# Create your models here.

class ProblemType(models.Model):
    image = models.ImageField(upload_to='service/media/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ServiceType(models.Model):
    image = models.ImageField(upload_to='service/media/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProblemReport(models.Model):
    STATUS_CHOICES = (
        ('reported', 'Reported'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    citizen = models.ForeignKey(User,on_delete=models.CASCADE, related_name='problem_report', limit_choices_to={'role': 'citizen'})
    problem_type = models.ForeignKey(ProblemType,on_delete=models.CASCADE)
    description = models.TextField(default="Need help")
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='reported')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.problem_type.name} by {self.citizen.username} - {self.status}"
    
class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    citizen = models.ForeignKey(User,on_delete=models.CASCADE, related_name='problem_request', limit_choices_to={'role': 'citizen'})
    service_type = models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    description = models.TextField(default="Need help")
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_type.name} by {self.citizen.username} - {self.status}"

