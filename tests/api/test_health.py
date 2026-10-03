import pytest
@pytest.mark.api
def test_health_endpoint(api_session,base_url):
    r=api_session.get(base_url+"/health"); assert r.status_code==200; assert r.json()["status"]=="healthy"
