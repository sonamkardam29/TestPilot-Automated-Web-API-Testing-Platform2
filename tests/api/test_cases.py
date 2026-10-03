import pytest
@pytest.mark.api
def test_get_test_cases(api_session,base_url):
    r=api_session.get(base_url+"/api/test-cases"); assert r.status_code==200; assert len(r.json())>=7
@pytest.mark.api
@pytest.mark.parametrize("test_id",[1,2,3])
def test_get_test_case_ids(api_session,base_url,test_id):
    r=api_session.get(base_url+f"/api/test-cases/{test_id}"); assert r.status_code==200
@pytest.mark.api
def test_invalid_test_case(api_session,base_url):
    r=api_session.get(base_url+"/api/test-cases/99999"); assert r.status_code==404
