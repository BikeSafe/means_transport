from transport_ms.models.transport_model import Transporte
from transport_ms.serializers.transport_serializer import TransportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class TransportList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Transporte.objects.all()
    serializer_class = TransportSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TransportDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Transporte.objects.all()
    serializer_class = TransportSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class TransportDetailUser(generics.ListAPIView):
    serializer_class = TransportSerializer
    def get_queryset(self):     
        id_usuario = self.kwargs['id_usuario']
        return Transporte.objects.filter(id_usuario=id_usuario)

