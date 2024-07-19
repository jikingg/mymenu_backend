from rest_framework import serializers
from .models import MealPost


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealPost
        fields = ('id', 'title', 'description', 'type', 'country', 'time', 'recipeURL', 'imageURL')

