from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
        def __str__(self):
                return self.nome_fantasia
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        primeiro_acesso = models.BooleanField(default=True)
        endereco = models.CharField(max_length=255, default='')
        celular = models.CharField(max_length=20, default='(00)00000-0000')
        telefone = models.CharField(max_length=20, default='(00)0000-0000')
        cpf = models.CharField(max_length=11, default='000.000.000-00')