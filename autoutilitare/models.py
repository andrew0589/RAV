from django.db import models

class Autoutilitare(models.Model):
    model = models.CharField(max_length=40)
    categorie = models.CharField(max_length=30)
    an_fabricatie = models.IntegerField()
    caroserie = models.CharField(max_length=30)
    combustibil = models.CharField(max_length=30)
    putere = models.CharField(max_length=30)
    capacitate_cilindrica = models.CharField(max_length=30)
    norma_poluare = models.CharField(max_length=30)
    greutate_maxima = models.IntegerField()
    cutie_de_viteza = models.CharField(max_length=30)
    numar_de_locuri = models.IntegerField()
    aer_conditionat = models.BooleanField(default=False)
    alarma = models.BooleanField(default=False)
    geamuri_electrice = models.BooleanField(default=False)
    inchidere_centralizata = models.BooleanField(default=False)
    servodirectie = models.BooleanField(default=False)
    navigatie = models.BooleanField(default=False)
    senzori_parcare = models.BooleanField(default=False)
    tractiune_integrala = models.BooleanField(default=False)
    camera_marsalier = models.BooleanField(default=False)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.model}'
