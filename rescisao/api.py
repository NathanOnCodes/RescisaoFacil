from ninja import Router
from django.shortcuts import get_list_or_404
from .schemas import FuncionarioSchemaIn, FuncionarioSchemaOut, ContratoSchemaIn
from .models import Contrato, Funcionario

router = Router()


@router.get("funcionarios/{id}/calculo-rescisao/", tags=["rescisao"])
def calcular_rescisao(request):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except Exception as e:
        return "Funcionário não encontrado", 404
    
    contratos_com_demissao = funcionario.contratos.filter(data_demissao__isnull=False)
    if not contratos_com_demissao:
        return 400, {"message": "O funcionário não possui contratos com data de demissão"}
    
    rescisoes = []
    for contrato in contratos_com_demissao:
        hora_trabalhada = contrato.salario / 8
        valor_rescisao =  (5 * (hora_trabalhada * 8)) * 0.4 + contrato.salario * 2
        rescisoes.append(
            {
                "cargo": contrato.cargo,
                "data_admissao": contrato.data_admissao,
                "data_demissao": contrato.data_demissao,
                "valor_rescisao": valor_rescisao
            }
            )
        
    return 200, {"rescisoes", rescisoes}


@router.post("/funcionarios", response= FuncionarioSchemaIn)
def criar_funcionario(request, funcionario: FuncionarioSchemaIn): # type: ignore
    try:
         novo_funcionario = Funcionario(**funcionario.dict())
         novo_funcionario.save()
         return 201, {"sucesso": "Novo funcionário criado"}
    except Exception as e:
         return "Funcionário ja existe", 400

@router.get("/funcionarios", response=list[FuncionarioSchemaOut])
def listar_funcionarios(request):
   try:
       return get_list_or_404(Funcionario.objects.all())
   except Exception as e:
       return "Você não cadastrou nenhum funcionário ou esta na rota sem permissão", 400
   

@router.get("/funcionarios/{id}", response=FuncionarioSchemaOut)
def detalhar_funcionario(request, id):
   try:
       return get_list_or_404(Funcionario.objects.filter(id=id))
   except Exception as e:
       return "Funcionário não encontrado", 404
      

@router.post("/funcionarios/{id}/contratos", response=ContratoSchemaIn)   
def criar_contrato(request, id, contrato: ContratoSchemaIn): # type: ignore
   try:
       novo_contrato = Contrato.objects.create(**contrato.dict())
       funcionario = Funcionario.objects.get(id=id)
       funcionario.contratos.add(novo_contrato)
       return 201, {"sucesso": "Novo contrato adicionado"}
   except Exception as e:
       return "Funcionário não encontrado", 404