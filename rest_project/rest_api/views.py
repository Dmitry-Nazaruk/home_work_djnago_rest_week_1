from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from datetime import datetime
from rest_api.models import Store
from rest_project.serializers import StoreSerializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(http_method_names=['GET'])
def today(request):
    return_dict = {'date': datetime.today().strftime('%d/%m/%Y'),
                   'year': datetime.today().strftime('%Y'),
                   'month': datetime.today().strftime('%m'),
                   'day': datetime.today().strftime('%d')}
    return Response(return_dict)


@api_view(http_method_names=['GET'])
def helloworld(request):
    return_dict = {'msg': 'Hello World'}
    return Response(return_dict)


@api_view(http_method_names=['GET'])
def helloworld(request):
    return_dict = {'msg': 'Hello World'}
    return Response(return_dict)


@api_view(http_method_names=['GET'])
def myname(request):
    name = request.query_params.get('name', 'anonymous')
    return Response({'name':name})


@api_view(http_method_names=['POST'])
def calculator(request):
    action = request.data.get('action')
    number1 = request.data.get('number1')
    number2 = request.data.get('number2')
    if action == 'minus':
        result = float(number1) - float(number2)
    elif action == 'plus':
        result = float(number1) + float(number2)
    elif action == 'divide':
        if number2 == 0:
            result = 'ZeroDivisionError'
        else:
            result = float(number1) / float(number2)
    elif action == 'multiply':
        result = float(number1) * float(number2)
    else:
        result = 'action has to be minus/plus/divide/multiply'
    return Response({'result': result})

@api_view(http_method_names=['GET'])
def all_store(request):
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['POST'])
def create_store(request):
    serializer = StoreSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Store.objects.create(**serializer.validated_data)
    return Response(status=HTTP_201_CREATED, data=serializer.data)


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

class StoreGenericViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

