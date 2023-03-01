from django.urls import include, path
from rest_framework import routers
from api.prima_servicios.views import PrimaView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/prima/<str:start>/<str:end>/<int:salary>', PrimaView.as_view())
]