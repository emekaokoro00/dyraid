from models import Meal, Meal_Type, Restaurant
from rest_framework import viewsets, serializers
from home.serializers import UserSerializer

class Meal_TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal_Type
        fields = ('meal_type_name', 'description')  

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'address')  
        
class MealSerializer(serializers.HyperlinkedModelSerializer):    
    user = UserSerializer(read_only=True)
    food_name = serializers.CharField(required=False, max_length=100)
    food_type = Meal_TypeSerializer(read_only=True)
    restaurant_offering = RestaurantSerializer(read_only=True)
    calories = serializers.IntegerField(required=False, default=0)
    
    class Meta:
        model = Meal
        fields = ('user', 'food_name', 'food_type', 'restaurant_offering', 'calories')   
        
    def create(self, validated_data):
        """
        Create and return a new Meal
        """ 
        return Meal.objects.create(**validated_data)
    
    