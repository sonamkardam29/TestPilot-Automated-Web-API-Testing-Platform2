import pytest
@pytest.mark.api
def test_summary_contract(api_session,base_url):
    r=api_session.get(base_url+"/api/summary"); assert r.status_code==200
    data=r.json()
    assert all(k in data for k in ["test_cases","test_runs","passed","failed","pass_percentage"])
@pytest.mark.api
def test_runs_endpoint(api_session,base_url):
    r=api_session.get(base_url+"/api/runs"); assert r.status_code==200; assert len(r.json())>=1
