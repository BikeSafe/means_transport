from rest_framework import serializers
from transport_ms.models.transport_model import Transport

class TransportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transport
        fields = ['id_transporte','id_usuario','tipo_transporte', 'carac_transporte', 'color_transporte']

    def create(self, validated_data):

        transport = Transport( id_usuario = validated_data.get("id_usuario"),
                          tipo_transporte = validated_data.get("tipo_transporte"),
                          carac_transporte = validated_data.get("carac_transporte"),
                          color_transporte= validated_data.get("color_transporte"))
        transport.save()
        return transport

    def update(self, instance, validated_data):
        instance.id_usuario = validated_data.get("id_usuario")
        instance.tipo_transporte = validated_data.get("tipo_transporte")
        instance.carac_transporte = validated_data.get("carac_transporte")
        instance.color_transporte = validated_data.get("color_transporte")
        instance.save()
        return instance

