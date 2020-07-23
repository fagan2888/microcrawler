from microprediction import MicroReader

def test_internet():
    mr = MicroReader()
    streams = mr.get_sponsors()
    assert len(streams)>10