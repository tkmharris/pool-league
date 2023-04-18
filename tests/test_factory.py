from PoolLeague import create_app
from PoolLeague.eight_ball import RESPONSES

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING':True}).testing

def test_eightball(client):
    response = client.get('/8ball')
    assert response.data.decode('utf8') in [
         f"Magic eight ball says ... {response}"
         for response in RESPONSES
    ]