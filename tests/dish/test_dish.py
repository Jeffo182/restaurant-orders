import pytest
from src.models.dish import Dish # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction

# Req 2
def test_dish():
    dish_name = "Lasanha"
    dish_price = 23.0
    #validando tipo
    with pytest.raises(TypeError):
        Dish(dish_name, "one")
    #valor negativo
    with pytest.raises(ValueError):
        Dish(dish_name, -23.0)
    #criando prato
    dish_lasagna = Dish(dish_name, dish_price)
    #verificando valores do prato
    assert dish_lasagna.name == dish_name
    assert dish_lasagna.price == dish_price
    assert dish_lasagna.recipe == {}
    #retornando em forma de string
    assert repr(dish_lasagna) == f"Dish('{dish_name}', R${dish_price:.2f})"
    #ingredientes na lista
    ingredients = [
        Ingredient("massa de lasanha"),
        Ingredient("queijo mussarela"),
        Ingredient("carne"),
    ]
    dish_lasagna.add_ingredient_dependency(ingredients[0], 3)
    dish_lasagna.add_ingredient_dependency(ingredients[1], 20)
    dish_lasagna.add_ingredient_dependency(ingredients[2], 10)

    assert dish_lasagna.get_ingredients() == set(ingredients)
    assert dish_lasagna.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.GLUTEN,
        Restriction.LACTOSE,
    }
    #verificando igualdade entre os objetos com hash
    dish_lasagna_2 = Dish(dish_name, dish_price)
    assert dish_lasagna == dish_lasagna_2
    assert hash(dish_lasagna) == hash(dish_lasagna_2)

    dish_lasagna_3 = Dish(dish_name, 24.0)
    assert dish_lasagna != dish_lasagna_3
    assert hash(dish_lasagna) != hash(dish_lasagna_3)
