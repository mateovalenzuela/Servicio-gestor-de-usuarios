from django.urls import path, include
from .views import GastosServiceView, DocsGastosServiceView

urlpatterns = [
    path('service_gastos/<path:path>', GastosServiceView.as_view(), name='service_gastos'),
    path('service_gastos_docs/', DocsGastosServiceView.as_view(), name='docs_service_gastos')
]