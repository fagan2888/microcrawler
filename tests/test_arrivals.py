
from microcrawler.arrivals import approx_mode

def test_approx_mode():
    xs = [1.0, 11.2, 13.3, 15.1, 13.7, 13.2]
    assert approx_mode(xs)==13