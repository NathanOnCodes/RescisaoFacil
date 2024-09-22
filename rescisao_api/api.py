from ninja import NinjaAPI
from rescisao.api import router as rescisao_router

api = NinjaAPI(title="Rescisão API", version="0.0.1")

api.add_router("/rescisao/", rescisao_router)