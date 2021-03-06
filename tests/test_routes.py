import json


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    excepted = {'hello': 'world'}
    assert excepted == json.loads(res.get_data(as_text=True))
