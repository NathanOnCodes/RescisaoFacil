from django.db import models

# Create your models here.
class Contrato(models.Model):
    cargo = models.CharField(max_length=100)
    data_admissao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cargo
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    cargo = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome