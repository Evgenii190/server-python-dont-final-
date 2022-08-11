from unicodedata import category
from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.core import serializers

from .serializers import ProductCategorySerializer, ProductCharacteristicSerializer, ProductSerializer, ProductSliderSerializer, ProductSubCategorySerializer
from .models import Characteristic, Product, ProductCategory, ProductCharacteristic, ProductSlider, ProductSubCategory, RequestMessage
from rest_framework.pagination import PageNumberPagination


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer
    lookup_field = 'category'
    def retrieve(self, request, category=None):
        queryset = ProductSubCategory.objects.filter(category=category)
        serializer = ProductSubCategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductsSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'subcategory'
    def retrieve(self, request, subcategory=None):
        queryset = Product.objects.filter(subcategory=subcategory)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination
    class Meta:
        ordering = ['id']

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(slug=slug)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductItemsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'products'
    def list(self, request):
        queryset = Product.objects.order_by("-id")
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, products=None):
        queryset = Product.objects.filter(category=products)[0:8]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductCharacteristicViewSet(viewsets.ModelViewSet):
    queryset = ProductCharacteristic.objects.all()
    serializer_class = ProductCharacteristicSerializer
    lookup_field = 'product'
    def retrieve(self, request, product=None):
        queryset = ProductCharacteristic.objects.filter(product_id=product)
        serializer = ProductCharacteristicSerializer(queryset, many=True)
        return Response(serializer.data)
    class Meta:
        ordering = ['id']

class ProductSliderViewSet(viewsets.ModelViewSet):
    queryset = ProductSlider.objects.all()
    serializer_class = ProductSliderSerializer
    lookup_field = 'product'

    def retrieve(self, request, product=None):
        queryset = ProductSlider.objects.filter(product_id=product)
        serializer = ProductSliderSerializer(queryset, many=True)
        return Response(serializer.data)

class RequestMessageAPIView(APIView):
    def post(self, request):
        new_requset = RequestMessage.objects.create(
            phone = request.data['phone'],
            address = request.data['address'],
            comment = request.data['comment'],
            mounting = request.data['mounting'],
            paymentMethod = request.data['paymentMethod']
        )
        return Response({'request': model_to_dict(new_requset)})

class ProductsQueryAPIView(APIView):
    parser_classes = [JSONParser]
    pagination_class = StandardResultsSetPagination
    class Meta:
        ordering = ['id']
    def post(self, request):
        data = request.data['filters'];
        category = request.data['category']
        # print(data)
        dict_pk = []

        productFilter = None;

        if category is not None:
            productsFilter = Product.objects.filter(subcategory=category);
        else:
            productsFilter = Product.objects.all();

        for product in productsFilter:
            cur = product.characteristics.all().values()
            for chx in cur:
                label = Characteristic.objects.get(id=chx['characteristic_id'])
                value = chx['value']
                for dataItem in data:
                    if value == dataItem['label']:
                        dict_pk.append(product)
        
        products = productsFilter

        filterProducts = products.filter(title__in=dict_pk);
        serializer = ProductSerializer(filterProducts, many=True)
        return Response({'data': {'results': serializer.data}})
