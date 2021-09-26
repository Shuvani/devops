import main
from main import app


def test__get__moscow__time__returns__string():
    moscow_time = main.get_moscow_time()
    assert type(moscow_time) == str


def test__get__moscow__time__returns__time():
    moscow_time = main.get_moscow_time()
    assert moscow_time[2] == ":"


def test__index__get_request__returns_200():
    # basic integration test
    request, response = app.test_client.get("/v11.0.0/")
    assert response.status == 200
