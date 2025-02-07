from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblProducts
        fields = ['id', 'productName', 'categoryID','product_ratting','old_price','current_price','description','productImage','productDate']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:        
        model = Category
        fields = ['id', 'categoryName','categoryImage','date_created']

class SildesSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblSlides
        fields = ['id', 'slideName', 'slideImage','slideDescription','smallslideDescription']

class SubTopMenuSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblSubTopMenu
        fields = ['id', 'subTopMenuName', 'subTopMenuImage','TopMenuID']

class TopMenuSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblTopMenu
        fields = ['id', 'topMenuName', 'topMenuImage']
