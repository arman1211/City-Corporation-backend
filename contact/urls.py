from django.urls import path
from .views import ContactPostView,ContactGetView

urlpatterns = [
    path('post/', ContactPostView.as_view(),name='contact-post'),
    path('get/', ContactGetView.as_view(),name='contact-get'),

]