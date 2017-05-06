import pytest
from fixture.aplication import Aplikacja


@pytest.fixture(scope="session")
def app(request):
    fixture = Aplikacja()
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
