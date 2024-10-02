from rest_framework.permissions import BasePermission

class IsCitizen(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'citizen'

class IsAuthority(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'authority'
