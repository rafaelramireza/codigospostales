from django.db import models

class CodigoPostal(models.Model):
    # Modelo para la tabla de códigos postales

    id_cp = models.IntegerField(primary_key=True)
    d_codigo = models.CharField(max_length=255)
    d_asenta = models.CharField(max_length=255)
    d_tipo_asenta = models.CharField(max_length=50)
    D_mnpio = models.CharField(max_length=255)
    d_estado = models.CharField(max_length=255)
    d_ciudad = models.CharField(max_length=255)
    d_CP = models.IntegerField()
    c_estado = models.IntegerField()
    c_oficina = models.CharField(max_length=255)
    c_CP = models.CharField(max_length=255)
    c_tipo_asenta = models.IntegerField()
    c_mnpio = models.IntegerField()
    id_asenta_cpcons = models.IntegerField()
    d_zona = models.CharField(max_length=50)
    c_cve_ciudad = models.CharField(max_length=50)

    # Método para representar el objeto como una cadena
    def __str__(self):
        return f"Código Postal: {self.d_codigo}, Asentamiento: {self.d_asenta}, Municipio: {self.D_mnpio}, Estado: {self.d_estado}"

    class Meta:
        # Especifica el nombre de la tabla en la base de datos
        db_table = 'codigopostal'
