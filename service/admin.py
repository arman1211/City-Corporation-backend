from django.contrib import admin
from .models import ProblemReport,ProblemType,ServiceType,ServiceRequest

# Register your models here.
admin.site.register(ProblemReport)
admin.site.register(ProblemType)
admin.site.register(ServiceType)
admin.site.register(ServiceRequest)
