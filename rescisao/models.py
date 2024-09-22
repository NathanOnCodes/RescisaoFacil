from django.db import models

class Contrato(models.Model):
    
    cargo: str = models.CharField(max_length=100)
    data_admissao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        

    def __str__(self):
        return self.cargo
    
    
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    contratos = models.ManyToManyField(Contrato, related_name='funcionarios')
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome