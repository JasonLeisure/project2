from django.contrib import admin
from recipes.models import Recipe, RecipeStep, Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "picture",
        "description",
        "id",
        "created_on",
    )


@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "step_number",
        "instruction",
        "recipe",
        "id",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "food_item",
        "recipe",
        "id",
    )
