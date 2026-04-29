from app import app 

def test_home(): 
    client = app.test_client() 
    response = client.get("/")
    assert response.status_code == 500
    assert response.data == b"Hello, CI/CD! I am Macmac! Your Lingkod from BSCS3A"