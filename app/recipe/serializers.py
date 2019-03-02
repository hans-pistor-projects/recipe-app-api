from rest_framework import serializers
from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serailzier for TAGS"""
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredients"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id', )


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipes"""

    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'tags',
                  'time_minutes', 'price', 'link')
        read_only_fields = ('id', )
