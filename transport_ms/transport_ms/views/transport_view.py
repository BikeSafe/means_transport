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

class TransportDetailUser(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Transporte.objects.all()
    serializer_class = TransportSerializer

    def get(self, request, *args, **kwargs):
        #usertransport = queryset(SELECT * FROM transport_ms_transporte WHERE transport_ms_transporte.id_usuario = %s)
        usertransport = Transporte.objects.extra(select={"select * from transport_ms_transporte where transport_ms_transporte.id_usuario = %s"},select_params=(someparam,),)
        return usertransport

