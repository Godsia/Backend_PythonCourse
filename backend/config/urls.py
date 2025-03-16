from django.urls import path, include
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as get_swagger_view
from drf_yasg import openapi

schema_view = get_swagger_view(
    openapi.Info(title="API", default_version='v1')
)

urlpatterns = [
    path('api/', include('app.urls')),
    path('swagger/', schema_view, name='swagger'),
]