from src.models.ingredient import Ingredient # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Criando objetos Ingredient com os mesmos ingredientes
    ingredient1 = Ingredient("Carne")
    ingredient2 = Ingredient("Carne")
    # Verificando as propriedades dos objetos Ingredient
    assert ingredient1.name == "Carne"
    assert hash(ingredient1) == hash("Carne")
    assert str(ingredient1) == "Ingredient('Carne')"
    assert ingredient1 == ingredient2
    assert ingredient1.restrictions == set()
