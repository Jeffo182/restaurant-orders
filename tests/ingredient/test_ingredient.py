from src.models.ingredient import Ingredient # noqa: F401, E261, E501


# Req 1
def test_ingredient():

    ingredient1 = Ingredient("carne")
    ingredient2 = Ingredient("frango")
    ingredient3 = Ingredient("carne")

    assert ingredient1.name == 'carne'
    assert ingredient1 != ingredient2
    assert ingredient1 == ingredient3
    assert hash(ingredient1) != hash(ingredient2)
    assert hash(ingredient1) == hash(ingredient3)
    assert str(ingredient1) == "Ingredient('carne')"
    assert ingredient1.restrictions == set()
