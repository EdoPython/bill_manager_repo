# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


# Create your models here.
class Bill(models.Model):
    metodo_choices = {
        'CA': 'Cash', # Efectivo
        'CC': 'Credit card', # Tarjeta
        'TR': 'Transfer', # Transferencia
        'PA': 'Paypal', # Paypal
        'CH': 'Check', # Cheque
        'OT': 'Other' # Otro
    }
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, editable=True)
    emisor = models.CharField(max_length=100)
    importe = models.DecimalField(max_digits=13, decimal_places=2)
    fechahora = models.DateTimeField(blank=False)
    metodo = models.CharField(
        max_length=2,
        choices=list(metodo_choices.items()),
        default='CA',
        blank=False
    )
    descripcion = models.TextField(blank=True)
    insercion = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return '[%s] %s : %s € (%s)' % (
            self.fechahora,
            self.emisor,
            '{:13.2f}'.format(self.importe).strip(),
            self.metodo_choices[str(self.metodo)]
        )
