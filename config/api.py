from ninja import NinjaAPI
from app.library.api.views import api

app = NinjaAPI(
    title='Bibliotech', description='Eficiencia na biblioteca escolar.'
)

app.add_router('/api', api, tags=['Books'])
