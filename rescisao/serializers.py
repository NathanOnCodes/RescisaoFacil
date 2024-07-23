from rest_framework import serializers # type: ignore
from rescisao.models import Contrato, Funcionario # type: ignore


class FuncionarioSerializer(serializers.ModelSerializer):
    class meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'salario': {'max_digits': 10, 'decimal_places': 2}
        }
        model = Funcionario
        fields = (
            'id',
            'nome',
            'cargo',
            'email',
            'telefone',
            'salario',
            'data_nascimento',
        )



class ContratoSerializer(serializers.ModelSerializer):
    class meta:
        extra_kwargs = {
            'cargo': {'write_only': True},
            'salario': {'max_digits': 10, 'decimal_places': 2}
        }
        model = Contrato
        fields = (
            'id',
            'cargo',
            'data_admissao',
            'data_demissao',
            'salario',
        )
