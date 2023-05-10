from rest_framework import serializers
from Our_site.models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'catalog')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'Название': data['name']}


class MenuSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)

class MenuMixin:
    def get_menu(self):
        menu = [
            {'title': 'Главная страница', 'url_name': 'Main'},
            {'title': 'Каталог', 'url_name': 'Catalog'},
            {'title': 'Поиск', 'url_name': 'Search'},
            {'title': 'Выбирете адрес', 'url_name': 'Address'},
            {'title': 'Корзина', 'url_name': 'Cart'},
            {'title': 'Контакты', 'url_name': 'Contacts'},
            {'title': 'Зайдите или зарегестрируйтесь', 'url_name': 'Login/Sign_up'}
        ]
        return MenuSerializer(menu, many=True).data

class HomeSerializer(serializers.Serializer):
    categories = CategorySerializer(many=True)
    menu = MenuSerializer(many=True)
    def get_categories(self, obj):
        return obj['categories'].values('name')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        if self.context.get('short'):
            return {
                'Название': instance.name,
                'Цена': instance.price,
                'Фотография': str(instance.image)
            }
        return super().to_representation(instance)
