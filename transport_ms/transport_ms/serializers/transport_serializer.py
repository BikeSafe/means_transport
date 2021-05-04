from rest_framework import serializers
from transport_ms.models.transport_model import Transporte

class TransportSerializer(serializers.ModelSerializer):

    tipo_transporte = serializers.ChoiceField(choices={"Bicicleta", "Patineta", "Scooter",})

    class Meta:
        model = Transporte
        fields = ['id_transporte','id_usuario','tipo_transporte', 'carac_transporte', 'color_transporte']

    def create(self, validated_data):

        um_long_to_short={"Bicicleta", "Patineta", "Scooter",}

        transporte = Transporte( id_usuario = validated_data.get("id_usuario"),
                          tipo_transporte = um_long_to_short[validated_data.get("tipo_transporte")],
                          carac_transporte = validated_data.get("carac_transporte"),
                          color_transporte= validated_data.get("color_transporte"))
        transporte.save()
        return transporte

    def update(self, instance, validated_data):
        um_long_to_short={"Bicicleta", "Patineta", "Scooter",}
        
        instance.id_usuario = validated_data.get("id_usuario")
        instance.tipo_transporte = um_long_to_short[validated_data.get("tipo_transporte")]
        instance.carac_transporte = validated_data.get("carac_transporte")
        instance.color_transporte = validated_data.get("color_transporte")
        instance.save()
        return instance
    
    def to_representation(self, obj):
        return {
            'id_usuario': instance ['id_usuario'],
            'tipo_transporte': instance ['tipo_transporte'],
            'carac_transporte': instance ['carac_transporte'],
            'color_transporte': instance ['color_transporte']
        }
