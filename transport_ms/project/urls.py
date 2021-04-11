from django.urls import path, include

urlpatterns = [
    path('', include('transport_ms.urls')),
]

