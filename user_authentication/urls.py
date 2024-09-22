from django.urls import path
from .views import CitizenRegisterView, AuthorityRegisterView,CustomTokenObtainPairView,LogoutView

urlpatterns = [
    path('register/citizen/', CitizenRegisterView.as_view(), name='register_citizen'),
    path('register/authority/', AuthorityRegisterView.as_view(), name='register_authority'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
]