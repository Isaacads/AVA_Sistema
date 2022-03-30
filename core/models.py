import email
from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=50)
    sala = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=150, blank=True)
    endereco = models.CharField(max_length=250, blank=True) 
    telefone = models.CharField(max_length=20, blank=True)
    celular = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome