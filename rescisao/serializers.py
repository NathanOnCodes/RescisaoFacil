from rest_framework import serializers # type: ignore
from .rescisao.models import Contrato, Funcionario # type: ignore


class FuncionarioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=100)
    data_nascimento = serializers.DateField()
    email = serializers.EmailField(null=True, blank=True)
    telefone = serializers.CharField(max_length=20, null=True, blank=True)
    cargo = serializers.CharField(max_length=100)

    def read_only_fields(self):
        return ['id']

    def create(self, validated_data):
        return Funcionario.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.email = validated_data.get('email', instance.email)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.cargo = validated_data.get('cargo', instance.cargo)
        instance.save()
        return instance

class ContratoSerializer(serializers.ModelSerializer):
    cargo = serializers.CharField(max_length=100)
    data_admissao = serializers.DateField()
    data_demissao = serializers.DateField(null=True, blank=True)
    salario = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Contrato.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.cargo = validated_data.get('cargo', instance.cargo)
        instance.data_admissao = validated_data.get('data_admissao', instance.data_admissao)
        instance.data_demissao = validated_data.get('data_demissao', instance.data_demissao)
        instance.salario = validated_data.get('salario', instance.salario)
        instance.save()
        return instance

