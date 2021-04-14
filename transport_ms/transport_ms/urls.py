from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from transport_ms.views.transport_view import TransportList
from transport_ms.views.transport_view import TransportDetail
from transport_ms.views.transport_view import TransportDetailUser

urlpatterns = [
    path('transportes/', TransportList.as_view()),
    path('transportes/<int:pk>', TransportDetail.as_view()),
    path('transporteusu/<int>', TransportDetailUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)