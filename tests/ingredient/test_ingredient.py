from src.models.ingredient import Ingredient # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Criando objetos Ingredient com diferentes ingredientes
    ingredient1 = Ingredient("carne")
    ingredient2 = Ingredient("frango")
    ingredient3 = Ingredient("bacon")
    # Verificando as propriedades dos objetos Ingredient
    assert ingredient1.name == "carne"
    assert ingredient2.name == "frango"
    assert ingredient3.name == "bacon"
    ingredient1_copy = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient1_copy
    assert ingredient1 != ingredient2
