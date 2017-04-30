import pytest
from fixture.aplikacja_grupy import Aplikacja_grupy



@pytest.fixture(scope = "session")
def app(request):
    fixture = Aplikacja_grupy()
    request.addfinalizer(fixture.destroy)
    return fixture

