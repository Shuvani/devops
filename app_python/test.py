import main
from main import app


def test__get__moscow__time__returns__string():
    moscow_time = main.get_moscow_time()
    assert type(moscow_time) == str


def test__index__get_request__returns_200():
    request, response = app.test_client.get("/v2.0.5/")
    assert response.status == 200
