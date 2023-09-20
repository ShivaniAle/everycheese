import pytest
from everycheese.users.models import User
from everycheese.cheeses.models import Cheese

pytestmark = pytest.mark.django_db

def test_user_get_absolute_url(user: User):
    url = f"/users/{user.username}/"
    assert user.get_absolute_url() == url
    
def test__str__():
    cheese = Cheese.objects.create(
        name="Stracchino",
        description="Semi-sweet cheese eaten with starches.",
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
