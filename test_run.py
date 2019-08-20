from run import app

def test_home():
    c = app.test_client()
    url = "/"
    response = c.get(url)
    assert response.status_code == 200
