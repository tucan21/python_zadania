import pytest
from fixture.aplikacja_grupy import Aplikacja_grupy
from fixture.aplikacja_kontakty import Aplikacja_kontakty


@pytest.fixture(scope = "session")
def app(request):
    fixture = Aplikacja_grupy()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope = "session")
def app(request):
    fixture = Aplikacja_kontakty()
    request.addfinalizer(fixture.destroy)
    return fixture