from datetime import date
from ninja.orm import create_schema
from ninja import Schema
from .models import Funcionario, Contrato


FuncionarioSchemaIn = create_schema(Funcionario)
FuncionarioSchemaOut = create_schema(Funcionario)
ContratoSchemaIn = create_schema(Contrato)
ContratoSchemaOut= create_schema(Contrato, exclude=["salario"])


