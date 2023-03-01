from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from commons.functions import validate_date
from api.prima_servicios.serializers import *

class PrimaView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    response_schema_dict = {
        "200": openapi.Response(
            description="custom 200 description",
            examples={
                "application/json": {
                    "200_key1": "200_value_1",
                    "200_key2": "200_value_2",
                }
            }
        ),
    }
    request_description = """
        start: Calculation start date in format YYYY-MM-DD, 
        end: Calculation end date in format YYYY-MM-DD, 
        salary: gross salary (without any discount), 
    """
    @swagger_auto_schema(operation_description=request_description, responses=response_schema_dict)
    def post(self, request, start, end, salary):
        try:
            dt_start = validate_date(start)
            dt_end = validate_date(end)
            return Response({'status':200, 'code':1, 'data':[dt_start, dt_end, salary]})
        except Exception as e:
            return Response({'message':e.args[0],'status':200, 'code':2, 'data':[]})