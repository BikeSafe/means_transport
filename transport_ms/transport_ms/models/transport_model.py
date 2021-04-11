from django.db import models

class Transport(models.Model):

    id_transporte = models.AutoField(primary_key = True)
    id_usuario= models.IntegerField(max_length = 10)
    tipo_transporte = models.CharField(max_length = 20)
    carac_transporte = models.CharField(max_length = 140)
    color_transporte = models.CharField(max_length = 20)

    class Meta:
        app_label = 'transport_ms'
