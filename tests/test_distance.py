from mlproject.distance import haversine

def test_haversine_float():
    assert type(haversine(48.865070,2.380009,48,2)) == float

def test_haversine_valeur():
    assert haversine(48.865070,2.380009,48.865070,2.380009)== 0
