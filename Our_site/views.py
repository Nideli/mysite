from django.http import HttpResponseNotFound, JsonResponse, HttpResponse
from django.db.models import Q
from django.views.decorators.http import require_GET
import json
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
from .serializers import *

class BaseAPI(MenuMixin):
    permission_classes = (IsAdminOrReadOnly,)
    def get_menu_data(self):
        return Response({
            'Меню': self.get_menu()
        })

class HomeAPI(BaseAPI,generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get(self, request):
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response({
           **{'Категории': categories_serializer.data},
            **self.get_menu_data().data
        })

class CategoryAPIDetailView(BaseAPI,generics.ListCreateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        category_serializer = CategorySerializer(category)
        products = Product.objects.filter(category=category)
        product_serializer = ProductSerializer(products, many=True, context={'short': True})
        return Response({
            **{'Категория': category_serializer.data},
            **self.get_menu_data().data,
            **{'Продукты': product_serializer.data}
        })


class Product_detail(BaseAPI, generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        product_serializer = ProductSerializer(product)
        return Response({
            **{'Продукт': product_serializer.data},
            **self.get_menu_data().data
        })

def product_detail(request):
    return HttpResponse(f'Отображение деталей продукта')


def cart(request):
    return JsonResponse({'message': 'Корзина'})


def checkout(request):
    return JsonResponse({'message': 'Оформление заказа'})


def order_detail(request):
    return JsonResponse({'message': 'Страница заказа'})


def profile(request):
    return JsonResponse({'message': 'Страница профиля пользователя'})


def order_history(request):
    return JsonResponse({'message': 'Страница истории заказов'})


def loginUser(request):
    return JsonResponse({'message': 'Страница входа'})


def logout_user(request):
    return JsonResponse({'message': 'Страница выхода'})


def register(request):
    return JsonResponse({'message': 'Страница регистрации'})


def payment(request):
    return JsonResponse({'message': 'Страница оплаты'})

@require_GET
def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query))
    categories = Category.objects.filter(Q(name__icontains=query))
    results = {}
    if products:
        product_results = []
        for product in products:
            product_results.append({
                'Название': product.name,
                'Цена': str(product.price),
                'Фото': str(product.image)
            })
        results['Продукты'] = product_results
    if categories:
        category_results = []
        for category in categories:
            products_in_category = category.product_set.all()
            product_results = []
            for product in products_in_category:
                product_results.append({
                    'Название': product.name,
                    'Цена': str(product.price),
                    'Фото': str(product.image)
                })
            category_results.append({
                'Категория': category.name,
                'Продукты': product_results,
            })
        results['Категории'] = category_results
    if not results:
        results = 'К сожалению, ничего не найдено'
    return HttpResponse(json.dumps(results), content_type='application/json')

def kontakti(request):
    return JsonResponse({'message': 'Здесь можно разместить ссылки на всякие контактики'})


def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не qwe</h1>')
