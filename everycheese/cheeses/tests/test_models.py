import pytest
from ..models import Cheese
from .factories import CheeseFactory

# Connects our tests with our database
pytestmark = pytest.mark.django_db

def test__str__():

    cheese = CheeseFactory(name="Stracchino")

    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
