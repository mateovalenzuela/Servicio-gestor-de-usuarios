import os
import json
import requests
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import action
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import FakeSerializer, GatewaySerializer


# Create your views here.


class GastosServiceView(GenericAPIView):
    service_host = settings.HOST_GASTOS_SERVICE
    permission_classes = [IsAuthenticated]
    serializer_class = GatewaySerializer

    path_param = openapi.Parameter(
        'path',
        openapi.IN_PATH,
        description="Path para consultar el servicio de gastos",
        type=openapi.TYPE_STRING,
        required=True,
    )

    def get_serializer_class(self):
        # Detectar si es una solicitud de generación de esquema
        if getattr(self, 'swagger_fake_view', False):
            return FakeSerializer
        return GatewaySerializer

    def validate_path(self, path):
        data_path = {'path': path}
        serializer = self.get_serializer(data=data_path)

        if not serializer.is_valid():
            return None, Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return path, None

    @swagger_auto_schema(manual_parameters=[path_param])
    def get(self, request, path, *args, **kwargs):
        path, error_response = self.validate_path(path)
        if error_response:
            return error_response

        url = f'{self.service_host}{path}'
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == status.HTTP_200_OK or status.HTTP_201_CREATED:
                return Response(response.json(), status=response.status_code)

            elif response.status_code == status.HTTP_400_BAD_REQUEST:
                return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

            elif response.status_code == status.HTTP_404_NOT_FOUND:
                return Response({'status': 404, 'title': "Not found"}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({'error': 'Error de servicio externo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except requests.exceptions.RequestException as e:
            return Response(f'Error en la solicitud: {str(e)}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(manual_parameters=[path_param])
    def post(self, request, path, *args, **kwargs):
        path, error_response = self.validate_path(path)
        if error_response:
            return error_response

        body = request.data
        url = f'{self.service_host}{path}'
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, json=body, headers=headers, verify=False)
            if response.status_code == status.HTTP_200_OK or status.HTTP_201_CREATED:
                return Response(response.json(), status=response.status_code)

            elif response.status_code == status.HTTP_400_BAD_REQUEST:
                return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

            elif response.status_code == status.HTTP_404_NOT_FOUND:
                return Response({'status': 404, 'title': "Not found"}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({'error': 'Error de servicio externo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except requests.exceptions.RequestException as e:
            return Response(f'Error en la solicitud: {str(e)}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(manual_parameters=[path_param])
    def put(self, request, path, *args, **kwargs):
        path, error_response = self.validate_path(path)
        if error_response:
            return error_response

        body = request.data
        url = f'{self.service_host}{path}'
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.put(url, json=body, headers=headers, verify=False)
            if response.status_code == status.HTTP_200_OK or status.HTTP_201_CREATED:
                return Response(response.json(), status=response.status_code)

            elif response.status_code == status.HTTP_400_BAD_REQUEST:
                return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

            elif response.status_code == status.HTTP_404_NOT_FOUND:
                return Response({'status': 404, 'title': "Not found"}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({'error': 'Error de servicio externo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except requests.exceptions.RequestException as e:
            return Response(f'Error en la solicitud: {str(e)}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(manual_parameters=[path_param])
    def delete(self, request, path, *args, **kwargs):
        path, error_response = self.validate_path(path)
        if error_response:
            return error_response

        body = request.data
        url = f'{self.service_host}{path}'
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.delete(url, json=body, headers=headers, verify=False)
            if response.status_code == status.HTTP_200_OK or status.HTTP_201_CREATED:
                return Response(response.json(), status=response.status_code)

            elif response.status_code == status.HTTP_400_BAD_REQUEST:
                return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

            elif response.status_code == status.HTTP_404_NOT_FOUND:
                return Response({'status': 404, 'title': "Not found"}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({'error': 'Error de servicio externo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except requests.exceptions.RequestException as e:
            return Response(f'Error en la solicitud: {str(e)}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DocsGastosServiceView(GenericAPIView):
    service_host = settings.HOST_GASTOS_SERVICE

    def get_serializer_class(self):
        # Detectar si es una solicitud de generación de esquema
        if getattr(self, 'swagger_fake_view', False):
            return FakeSerializer
        return None

    def get(self, request):

        url = f'{self.service_host}swagger/v1/swagger.json'
        try:
            response = requests.get(url, headers={'Content-Type': 'application/json'}, verify=False)
            response.raise_for_status()
            return Response(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud a {url}: {str(e)}")
            return Response(f'Error en la solicitud: {str(e)}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
