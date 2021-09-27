import main
from main import app


def test__get__moscow__time__returns__string():
    moscow_time = main.get_moscow_time()
    assert type(moscow_time) == str


def test__get__moscow__time__returns__time():
    moscow_time = main.get_moscow_time()
    assert moscow_time[2] == ":"
